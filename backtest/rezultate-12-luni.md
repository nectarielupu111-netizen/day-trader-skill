# Backtest ORB pe 12 luni – 61 acțiuni/ETF-uri, Alpaca IEX, 27 oct 2025 – 27 oct 2026

Date: 13.537 sesiuni complete (89%). Acoperire slabă: GS, COST, ABNB, UAL, ABBV (89–135 sesiuni). Slippage 2 bps.

## 7 variante de bază
| Variantă | Tranzacții | Winrate | Expectancy | Total | PF |
| --- | --- | --- | --- | --- | --- |
| Long 1R | 7884 | 49.1% | -0.069R | -547.3R | 0.85 |
| Long 2R | 7884 | 40.6% | -0.056R | -437.9R | 0.90 |
| Short 1R | 7862 | 49.0% | -0.073R | -577.4R | 0.85 |
| Long+short 1R | 15746 | 49.1% | -0.071R | -1124.7R | 0.85 |
| Long+short 2R | 15746 | 40.6% | -0.055R | -862.2R | 0.90 |
| Long 1R, stop margine range | 7884 | 48.6% | -0.032R | -250.3R | 0.91 |
| Long 0.5R | 7884 | 63.6% | -0.083R | -656.9R | 0.76 |

## Căutare filtre (864 combinații; in-sample 27 oct 2025–30 iun 2026, out-of-sample 1 iul–27 oct 2026)
Top in-sample (>=150 tranzacții): toate short. Cel mai bun: short 2R, stop mijloc range, gap ≥2%, trend SPY: 231 tranzacții, 45.5%, +0.069R, PF 1.14.
VWAP nu schimbă nimic.

Out-of-sample (rulat o singură dată):
| Configurație | Tranzacții | Winrate | Expectancy | PF |
| --- | --- | --- | --- | --- |
| short 2R gap≥2% trend SPY | 119 | 40.3% | -0.015R | 0.97 |
| short 2R rvol≥1.5 trend SPY range≤1.5% | 71 | 54.9% | +0.239R | 1.56 |
| short 2R gap≥2% | 170 | 40.0% | -0.038R | 0.93 |

## Concluzie
ORB pierde pe un an în toate variantele de bază. Edge-ul găsit in-sample e mic și dispare out-of-sample. Singurul câștigător OOS are 71 de tranzacții după 864 de combinații testate: probabil noroc statistic. Winrate 80% nu apare nicăieri; winrate mare vine doar cu ținte mici și expectancy negativ.
Fișiere pe PC: C:\Users\User\day-trading (results_12m.md, orb_backtest.py, grid_search.py, data_alpaca\).
