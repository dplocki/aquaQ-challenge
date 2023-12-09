# It's alive

Today we hunt the most dangerous game: cellular automata.

Cellular automata are on-off (or living-dead) states in each cell on a grid which iterate step-by-step depending only on the current state of each cell and its neighbours. Here, neighbours are considered the cell above, below, left, and right of the current cell - no diagonals. The rules for iteration in this system are as follows:
* If a cell has an even number of surrounding "on" states, it should be set to (or remain) off.
* If a cell has an odd number of surrounding "on" states, it should be set to (or remain) on.
Points outside the boundary are considered to be "off".

Your input is multiple sets of run times, square grid widths, and the matrix index pairs of starting cells (0,0 is the top left corner, etc)

For each input row, after constructing the start state and running for the required number of steps, you need to find how many are alive.
For example, with input:

```txt
350 6 2 2 2 3
```

First construct a grid with width and height 6, and set points (2,2) and (2,3) as "on":

```txt
......
......
..##..
......
......
......
```

This is the state at time 0. For times 1, 2, and 3 we iterate as below:

```txt
......
..##..
.####.
..##..
......
......

..##..
......
##..##
......
..##..
......

.####.
######
######
######
.####.
..##..
```


After 350 steps, we arrive at this state

```txt
.#..#.
......
.#..#.
......
#.##.#
......
```

For this input, the answer is 8.
What is the sum of the living cells after the required run time for each input?
