# Bit of Bully

After a hard day shopping, in a real shop, openly, on a street, taking this action entirely for granted, you have decided to visit the local pub. Which you also take for granted.

An indeterminate amount of pints in, you realise you've hit the perfect peak for a spot of darts. You pick up your arrows, make your way over to the board, and realise that it's staring you down. Not one to shy away from a challenge, you decide to teach this dartboard a lesson and set yourself a series of points targets. You realise that, while time outside seems to have stopped and the days have blended into one, it might be useful to estimate how many darts you'll need to throw, just in case.

Your game is naturally completely flawless, so what is the minimum number of darts will you need to hit the exact score in your input, and in a separate game for each, every number on the way there? You're just aiming to get a total number of points, not paying attention to any other rules about e.g. finishing on a double.

A single dart can score all the numbers from 1 to 20

```txt
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
```

as well as the doubles and triples of those numbers on the double score and triple score segments,

```txt
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40
3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60
```

and in the bullseye:

```txt
25 50
```

For example, if your input is 30, you would play a game with point target 1, another with point target 2, ..., all the way to a game with points target 30. Your answer will be 32 - one dart for any number except 23 and 29, which require two each, through whatever combination of available numbers.
