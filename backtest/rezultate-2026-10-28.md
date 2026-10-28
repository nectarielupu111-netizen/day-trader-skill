# Backtest ORB (breakout din primele 15 minute) – primul test, 2026-10-28

Date: TSLA, bare de 5 minute, 59 sesiuni complete până la 19 oct 2026 (singurele date disponibile offline, din testele repo-ului day-trader-skill).
Reguli: intrare la prima bară care închide peste maximul (long) / sub minimul (short) primelor 15 minute, între 9:45 și 15:30; stop la mijlocul range-ului; ieșire forțată la 15:55; slippage 2 bps pe intrare și ieșire.
Validare: varianta long 1R reproduce exact cifrele repo-ului (33 semnale, 13 target, 15 stop, 5 la închidere).

| Variantă | Tranzacții | Winrate | Expectancy / tranzacție | Profit factor |
| --- | --- | --- | --- | --- |
| Long, target 1R | 33 | 42.4% | -0.12R | 0.77 |
| Short, target 1R | 26 | 42.3% | -0.17R | 0.61 |
| Long + short, 1R | 59 | 42.4% | -0.14R | 0.71 |
| Long, target 2R | 33 | 33.3% | -0.22R | 0.63 |
| Short, target 2R | 26 | 30.8% | -0.25R | 0.52 |
| Long + short, 2R | 59 | 32.2% | -0.23R | 0.58 |

Concluzie: pe TSLA, în această perioadă, strategia pierde în toate variantele. Un singur ticker și 59 de zile nu ajung pentru o concluzie generală; următorul pas e același test pe 50–100 de acțiuni și 6–12 luni de date (Alpaca).

Script: /mnt/project-files/backtest/orb_backtest.py

## Al doilea test: 61 de acțiuni și ETF-uri, 5 aug – 28 oct 2026 (Yahoo, 5 min, 3.599 sesiuni)

| Variantă | Tranzacții | Winrate | Expectancy | Total | PF |
| --- | --- | --- | --- | --- | --- |
| Long, 1R | 1905 | 46.5% | -0.110R | -209.3R | 0.77 |
| Long, 2R | 1905 | 40.2% | -0.111R | -211.6R | 0.79 |
| Short, 1R | 1963 | 46.0% | -0.117R | -229.2R | 0.76 |
| Long + short, 1R | 3868 | 46.3% | -0.113R | -438.5R | 0.76 |
| Long + short, 2R | 3868 | 39.8% | -0.108R | -416.2R | 0.80 |
| Long, 1R, stop la marginea range-ului | 1905 | 46.7% | -0.055R | -103.9R | 0.83 |
| Long, 0.5R | 1905 | 62.3% | -0.090R | -170.7R | 0.75 |

Concluzie: ORB simplu nu are edge pe această perioadă. Un target mai mic crește winrate-ul (62% la 0.5R), dar expectancy-ul rămâne negativ. Date pe PC: C:\Users\User\day-trading\data.
