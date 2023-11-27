# What is best in life?

Elo is a method of tracking historical performance and estimating the chances of future success in head-to-head matchups - it was made for chess, but can be applied to lots of sports and video games. We'll use it here to see who's been performing best in a display of god-like athleticism: the AquaQ table tennis tournament.

The way Elo works is by comparing the expected win rate of two head-to-head competitors, calculated for player a with:

```txt
Ea = 1 / (1 + 10^((Rb-Ra)/400))
```

Here, Ra and Rb are the ratings of teams a and b - which start at 1200 and are modified with:

```txt
Ri' = Ri + 20(1-Ei)
```

where Ri is the old ranking, and Ri' is the updated ranking for the winning team - 20(1-Ei) is the amount of points the winner gains and the loser loses. For example, if Ra is 1400 and Rb is 1200, a has an expected win rate of around 0.75 over b, and if a wins, Ra gains, and Rb loses, about 5 points each. Conversely if b wins, b gains and a loses 15 points.

This dependency on the point ratings ensures that an expected result doesn't change points distribution too much, but an unexpected result causes a larger points swing.

To answer this challenge, take the input csv of table tennis games, and find the difference between the best and worst Elo in the final standings. You'll need to work out who won in each game and update their rating after every match. When calculating the final value, use only the integer part of the highest and lowest values, e.g.

```txt
1500.89-913.1
```

becomes

```txt
1500-913
```