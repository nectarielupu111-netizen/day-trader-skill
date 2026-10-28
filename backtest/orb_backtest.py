#!/usr/bin/env python3
"""Opening-range breakout backtest on 5-minute bars.

Rules (same as day-trader-skill's defaults, plus a short side and costs):
  - opening range = first 15 minutes (9:30, 9:35, 9:40 bars), full sessions only
  - entry: first bar after the range that CLOSES above the range high (long)
    or below the range low (short), at that bar's close, between 9:45 and 15:30
  - stop: range midpoint (or range low/high with --stop or-edge)
  - target: R times the risk (--target-r, default 2)
  - a bar that touches both stop and target counts as the stop
  - flat at the 15:55 bar's open if neither hit
  - costs: --slippage-bps on entry and exit, --commission per share per side

Input: Yahoo chart JSON files (.json or .json.gz), one per symbol, or a
directory of them. Alpaca bars can be added as another loader later.

  python3 orb_backtest.py DATA_DIR_OR_FILES --target-r 2 --side both
"""
import argparse
import gzip
import json
import os
from collections import defaultdict
from datetime import datetime, timedelta, timezone

NY_STD, NY_DST = timedelta(hours=-5), timedelta(hours=-4)


def ny_offset(utc):
    # US DST: second Sunday of March 07:00 UTC to first Sunday of November 06:00 UTC
    y = utc.year
    mar = datetime(y, 3, 8, tzinfo=timezone.utc)
    start = mar + timedelta(days=(6 - mar.weekday()) % 7, hours=7)
    nov = datetime(y, 11, 1, tzinfo=timezone.utc)
    end = nov + timedelta(days=(6 - nov.weekday()) % 7, hours=6)
    return NY_DST if start <= utc < end else NY_STD


def load_yahoo(path):
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt") as f:
        d = json.load(f)
    r = d["chart"]["result"][0]
    q = r["indicators"]["quote"][0]
    sym = r["meta"]["symbol"]
    days = defaultdict(list)
    for i, ts in enumerate(r.get("timestamp") or []):
        o, h, l, c = q["open"][i], q["high"][i], q["low"][i], q["close"][i]
        if None in (o, h, l, c):
            continue
        utc = datetime.fromtimestamp(ts, timezone.utc)
        local = utc + ny_offset(utc)
        mins = local.hour * 60 + local.minute
        if 570 <= mins < 960:  # 9:30 to 16:00
            days[local.date()].append((mins, o, h, l, c))
    return sym, {d: sorted(b) for d, b in days.items() if len(b) == 78}


def run_day(bars, side, target_r, stop_rule, entry_from=585, entry_until=930, flat_at=955):
    rng = [b for b in bars if b[0] < 585]
    orh, orl = max(b[2] for b in rng), min(b[3] for b in rng)
    mid = (orh + orl) / 2
    for i, (m, o, h, l, c) in enumerate(bars):
        close_time = m + 5
        if m < 585 or close_time < entry_from or close_time > entry_until:
            continue
        if side == "long" and c > orh:
            entry, stop = c, (mid if stop_rule == "or-mid" else orl)
        elif side == "short" and c < orl:
            entry, stop = c, (mid if stop_rule == "or-mid" else orh)
        else:
            continue
        risk = abs(entry - stop)
        if risk <= entry * 0.0005:
            return None
        sgn = 1 if side == "long" else -1
        target = entry + sgn * target_r * risk
        for (m2, o2, h2, l2, c2) in bars[i + 1:]:
            if m2 >= flat_at:
                return dict(side=side, entry=entry, stop=stop, exit=o2, risk=risk, how="close")
            hit_stop = l2 <= stop if sgn > 0 else h2 >= stop
            hit_tgt = h2 >= target if sgn > 0 else l2 <= target
            if hit_stop:
                # a gap through the stop fills at the open, not at the stop
                fill = min(o2, stop) if sgn > 0 else max(o2, stop)
                return dict(side=side, entry=entry, stop=stop, exit=fill, risk=risk, how="stop")
            if hit_tgt:
                return dict(side=side, entry=entry, stop=stop, exit=target, risk=risk, how="target")
        return dict(side=side, entry=entry, stop=stop, exit=bars[-1][4], risk=risk, how="close")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--side", choices=["long", "short", "both"], default="long")
    ap.add_argument("--target-r", type=float, default=2.0)
    ap.add_argument("--stop", choices=["or-mid", "or-edge"], default="or-mid")
    ap.add_argument("--slippage-bps", type=float, default=2.0)
    ap.add_argument("--commission", type=float, default=0.0, help="USD per share per side")
    ap.add_argument("--trades", action="store_true", help="print every trade")
    a = ap.parse_args()

    files = []
    for p in a.paths:
        if os.path.isdir(p):
            files += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.endswith((".json", ".json.gz"))]
        else:
            files.append(p)

    sides = ["long", "short"] if a.side == "both" else [a.side]
    trades = []
    sessions = 0
    for f in files:
        sym, days = load_yahoo(f)
        sessions += len(days)
        for d in sorted(days):
            for s in sides:
                t = run_day(days[d], s, a.target_r, a.stop)
                if t:
                    sgn = 1 if s == "long" else -1
                    slip = (t["entry"] + t["exit"]) * a.slippage_bps / 1e4
                    gross = sgn * (t["exit"] - t["entry"])
                    net = gross - slip - 2 * a.commission
                    t.update(sym=sym, date=str(d), r=net / t["risk"])
                    trades.append(t)

    if a.trades:
        for t in trades:
            print("%s %-5s %-5s entry %.2f stop %.2f exit %.2f %-6s %+.2fR" % (
                t["date"], t["sym"], t["side"], t["entry"], t["stop"], t["exit"], t["how"], t["r"]))
    n = len(trades)
    print("symbols %d, full sessions %d, trades %d (%s, target %.1fR, stop %s, slippage %.1f bps, commission $%.3f/share)"
          % (len(files), sessions, n, a.side, a.target_r, a.stop, a.slippage_bps, a.commission))
    if not n:
        return
    wins = [t["r"] for t in trades if t["r"] > 0]
    losses = [t["r"] for t in trades if t["r"] <= 0]
    pf = sum(wins) / -sum(losses) if losses and sum(losses) < 0 else float("inf")
    by_how = defaultdict(int)
    for t in trades:
        by_how[t["how"]] += 1
    print("winrate %.1f%%  expectancy %+.3fR per trade  total %+.1fR  profit factor %.2f"
          % (100 * len(wins) / n, sum(t["r"] for t in trades) / n, sum(t["r"] for t in trades), pf))
    print("exits: " + ", ".join("%s %d" % kv for kv in sorted(by_how.items())))


if __name__ == "__main__":
    main()
