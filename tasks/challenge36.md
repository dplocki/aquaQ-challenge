# Tetonor Terror

Continuing to wander the station after [decrypting an entire book](./challenge35.md), you notice a flurry of activity headed your way. Several of the local constabulary have decided to take issue with your seemingly simple understaning of sensitive documents. The man in charge demands you prove at once that you are not a robot, android, or other automaton. Upon asking him how you would go about this, he produces several pages of grids and numbers, and asks you to solve some puzzles. You wonder if this man knows what robots are.

The puzzles to be solved are know as tetonors. Each puzzle consists of a 4-by-4 grid of numbers:

```txt
252 260 13  30
25  144 36  30
48  21  40  30
224 56  46  22
```

Beneath this grid is a series of input numbers in ascending order:

```txt
1 2 2 5 6 6 8 10 14 16 21 23 24 26 28 42
```

Brief instructions at the top indicate your goal is to find pairs of input numbers such that each pair has a sum which contributes to one grid number, and a product which contributes to another. For example, the pair 42, 6 gives grid answers 252 (42 * 6) and 48 (42 + 6). Each entry in the input number list can be used only once, so you would expect to see one pair with a 1 in it, 2 pairs with a 2 in them (or one pair with two 2s!), 1 pair with a 5, etc.
After building the pairs and evaluating which will give the correct answer, you write down the set of 8 pairs which will give the 16 grid numbers, like so:

```txt
42 6
10 26
8  5
28 2
23 2
24 6
21 1
16 14
```

Looking more closely, you see the "answer" for this grid is the sum of the absolute differences of the pairs, which in this case is 36 + 16 + 3 + 26 + 21 + 18 + 20 + 2 = 142.

You realise that, on the rest of the pages, some of the input numbers are redacted, replaced with *. You look back to the puzzle master, twiddling his moustache in an oddly[-](./challenge32.md)familiar gesture. You set about solving these problems to demonstrate you are not a member of the notoriosly dyscalculiaic robot scourge.

Your challenge inputs, the remaining grids, are of the form:

```txt
g:grid numbers
i:redacted inputs
```

Each pair of grid/inputs is separated with a blank line. Determine the answer as above for each grid in your input file; the sum of these is the answer to this challenge.