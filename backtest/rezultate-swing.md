# Backtest swing – date zilnice Alpaca SIP, 61 acțiuni, ian 2016 – oct 2026

Long only, intrare la deschiderea zilei următoare, slippage 5 bps/parte, max 10 poziții x 10%. In-sample 2016–2022, out-of-sample ian 2023 – oct 2026.

| Strategie (cea mai bună IS) | Perioadă | Tranzacții | Winrate | Medie/tranz. | PF | CAGR | Max DD | Expunere |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 pullback RSI(2)<5, ieșire > SMA5 | IS | 1035 | 65.0% | +0.44% | 1.49 | +6.5% | 10.6% | 22% |
| | OOS | 791 | 61.9% | +0.46% | 1.38 | +9.4% | 12.1% | 32% |
| S2 3 zile în scădere | IS | 2005 | 65.7% | +0.31% | 1.32 | +8.6% | 22.1% | 41% |
| | OOS | 1466 | 63.2% | +0.25% | 1.20 | +9.3% | 15.7% | 56% |
| S3 breakout maxim 20 zile, stop trailing 3xATR | IS | 470 | 46.8% | +3.00% | 2.23 | +19.7% | 12.8% | 75% |
| | OOS | 350 | 42.0% | +2.84% | 1.78 | +20.6% | 23.1% | 90% |
| S4 rotație momentum top 10 | IS | 362 | 53.6% | +3.46% | 2.32 | +14.7% | 25.7% | 66% |
| | OOS | 281 | 51.2% | +4.72% | 2.45 | +31.7% | 28.1% | 92% |
| SPY buy & hold | IS | | | | | +11.5% | 33.8% | 100% |
| | OOS | | | | | +21.5% | 18.8% | 100% |

Concluzie: toate 4 rămân profitabile out-of-sample (spre deosebire de intraday). Winrate maxim cu profit: 62–66% (S1/S2); 80% nu apare. Atenție: lista de 61 de acțiuni e aleasă azi (survivorship bias), ceea ce umflă mai ales S3/S4.
