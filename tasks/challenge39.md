# Game of Throwns

It's that time [again](./challenge33.md). You stride boldly down to the nearest dart enjoyers association, ready for a rousing few thousand throws. Unfortunately, the local is closed due to severe and irreparable crimes against hygiene. Luckily for you, someone has left an extremely detailed record of the last several thousand darts thrown just sitting there. These numbers are a portal directly to hours of enjoyment; imagined pints and arrows flying. Bliss.

An example number trace from thrown darts looks like so:

```txt
11 38 9 25 24 15 50 10 8 40 17 24 10 6 10 38 6 12 32 19 16 18 16 51 39 34 24 4 54 9 6 32 51 11 1 30 3 12 40 32 9 14 2 3 36 12 60 42 33 1 6 45 36 5 21 57 4 51 30 11 7 36 20 24 14 28 54 17 18 12 18 36 10 38 16 18 7 27 12 34 40 9 16 25 22 15 15 20 8 12 13 16 4 57 39 11 13 40 5 33 36 36 1 54 45 19 3 18 30 57 5 3 8 9 40 3 40 9 17 60 26
```

As expected, all the players are excellent and never miss. Each player starts with 0 points, and the goal is to get to 501 by adding each throw to the current player's total. A leg of darts consists of each player throwing three darts, then handing over to the other player. When a player hits 501 points, they win that leg, and the next starts immediately. Players alternate being first on each leg.

For example, in the trace above, the starting player (let's call them player A) throws 11, 38, 9 in their first turn, giving a total of 58. The next three darts are 25, 24, 15, from the second player (player B), scoring 64. The leg finishes with the starting player throwing the 45th overall dart, with a score of 36. So player B starts the second leg by throwing 12 60 42, it ends after 38 total darts, with player B winning.

The challenge is, from the input below, to determine how many legs player A wins, and multiply that by the sum of the value of the winning dart in each leg. In the example above, player A wins 2 legs, and the sum of the final darts in each leg are 36 + 16 + 26. This gives a final score of 156 (2*78).
