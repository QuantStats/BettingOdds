**Work in progress... More contents to be added in the future.**

The script `PythonBettingOdds.py` computes and plots the decimal-odd decay function as witnessed on betting exchanges when the score remains at 0-0 throughout the 90 minutes of a soccer match. The underlying assumption is that the goal arrival follows a Poisson process. With a scoring intensity of 3, i.e. the expected total goals in a match is three, the decay function will look as follows,

![alt text](https://github.com/QuantStats/BettingOdds/blob/master/decimal_odd.png)

As illustrated above, the odd decay function for any under-goal market has to be decreasing to satisfy the no-arbitrage argument: at the start of the match (*t*=0), the probability of the score to remain under *n* goals is low, a higher decimal odd has to be offered to compensate for the higher risk; as the match progresses, the probability of the score to remain under *n* goals increases, a lower decial odd has to be offered for the lower risk. The boundary condition is that at the end of the match (*t*=90), the decimal odd has to be equal to one, i.e. if one bets a dollar, the dollar will be returned because the probability of under *n* goals is always one at the boundary, or in other words, there is no risk.

In a similar fashion, for *n*<*m*, the decay curve for an under *n*-goal market is higher than the decay curve for an under *m*-goal market at any time point, *t*. This is also due to the no-arbitrage argument where a lower *n* means more risk is taken, which translates to a higher compensation in the form of a higher decimal odd offering.
