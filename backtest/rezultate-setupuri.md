# Alte setup-uri intraday – 12 luni Alpaca, 61 acțiuni (in-sample 27 oct 2025–30 iun 2026, OOS 1 iul–27 oct 2026)

81 de configurații, slippage 2 bps, intrări 9:45–15:30, ieșire 15:55.

## Cea mai bună configurație pe familie (in-sample)
| Familie | Configurație | Tranzacții | Winrate | Expectancy | PF |
| --- | --- | --- | --- | --- | --- |
| Fade de gap | long, gap jos ≥2%, țintă închiderea de ieri | 312 | 59.0% | +0.134R | 1.51 |
| Revenire la VWAP | long K=1.5, țintă VWAP | 6631 | 38.5% | -0.212R | 0.72 |
| Pullback în trend (EMA20) | long 2R | 2916 | 36.1% | -0.189R | 0.75 |
| Reversie RSI | short RSI3>95, ieșire RSI 50 | 387 | 58.9% | -0.027R | 0.92 |

## Top 3 out-of-sample (rulat o singură dată)
| Configurație | Tranzacții | Winrate | Expectancy | PF |
| --- | --- | --- | --- | --- |
| gap-fade long ≥2%, țintă închiderea de ieri | 170 | 51.2% | -0.017R | 0.94 |
| gap-fade long ≥2%, 2R | 195 | 48.2% | +0.019R | 1.06 |
| gap-fade long ≥2%, 1R | 195 | 49.2% | +0.002R | 1.01 |

## Concluzie
Doar fade-ul de gap long arată edge in-sample, iar out-of-sample scade la ~0. Nicio familie nu se apropie de 80% winrate cu expectancy pozitiv (maxim 59% in-sample, 51% OOS).
