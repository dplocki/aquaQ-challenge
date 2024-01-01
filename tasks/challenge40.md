# Prominence promenade

Breathe deeply. Drink in the crisp air. But wait, what's that? It smells precisely like one dozen bears. You're in the middle of an extremely large mountain range, and now you need to climb over all the peaks as quickly as possible. To do so, you need to find the peaks in the mountain range, and how much effort you'll need to spend climbing them.

You have a map of the mountain range handily condensed into a string of numbers, representing the heights of the range. For example:

```txt
0 1 2 4 6 8 9 8 6 4 2 3 5 6 5 4 5 7 8 6 4 2 1 0
```

Looks like, with the peaks relabelled to A, B, C:

```txt
      A
     888          C
     777         77
    66666    B   666
    55555   555 5555
   4444444  444444444
   3333333 3333333333
  22222222222222222222
 1111111111111111111111
000000000000000000000000
```

To estimate how much work you need to do to clamber over all of them at ideally faster than 60 km/h, you need to find the prominences. These are the smallest drop in height from a summit to reach higher or (in our case) equal-height ground.

For example, peak A is the highest. From here, you can't reach higher ground, so it has a prominence that is its own height, i.e. 9.
Peak B has a prominence of 2. You can reach higher ground by going to A (dropping 4 in height to climb up) or C (dropping 2).
Peak C has a prominence of 6. You need to go to the first peakl to reach another height of 8, so you must drop by 6.

Non-peak numbers have no prominence, or prominence 0. If you were to evaluate the prominences of every height in your map above, you would get the following:

```txt
0 0 0 0 0 0 9 0 0 0 0 0 0 2 0 0 0 0 6 0 0 0 0 0
```

In your desperation to escape twelve (12) bears, you need to know the total prominence you'll have to cover - the sum of all the peak prominences . In the above example, this is 17.

A slightly more complex example is:

```txt
0 1 3 4 6 5 6 5 7 5 6 7 6 4 2 0 1 0 2 4 5 4 3 4 2 4 5 3 5 7 5 7 8 10 11 13 11 9 10 9 7 8 7 8 9 10 8 7 8 6 7 6 4 2 0
```

Which has a prominence sum of 35.

For your input below, what is the sum of the prominences?