# Number Neighbours

You awake with a start, having fallen asleep on a particularly comfy bench. You dreamt of numbers, and in the dream, they told you how they estimate their own comfort.

Numbers in a list like being part of a streak which sums to a multiple of the length of the streak. e.g. A number in the list

```txt
1 3 2
```

is generally very comfortable because it's in a streak of 3 (the whole list) which sums to a multiple of 3 (in this case, 6).
Each number also is part of other streaks which are comfortable:

```txt
1 is part of a streak of 1 which sums to 1 (a multiple of 1)
1 is part of a streak of 2 which sums to 4 (a multiple of 2)
1 is part of a streak of 3 which sums to 6 (a multiple of 3)

3 is part of a streak of 1 which sums to 3 (a multiple of 1)
3 is part of a streak of 2 which sums to 4 (a multiple of 2)
3 is part of a streak of 2 which sums to 5 (oh dear - very uncomfortable)
3 is part of a streak of 3 which sums to 6

2 is part of a streak of 1
2 is part of the streak of 2 summing to 5 (see above re:discomfort)
2 is part of the streak of 3 summing to 6
```

Each number in the list evaluates its streaks in ascending order, and in order to feel both comfortable AND cosy, it checks for the length of the unbroken streak of comfortable streaks. So, 1 has a streak of 3 (as it's part of a list of 1, 2, and 3 elements which are comfortable). 3 has a streak of 3, too, as even though it has one uncomfortable streak of 2, it has another comfortable one. 2 only has a streak of 1 - even though it has a comfortable 3-streak, it can't get past 1 without feeling uncomfortable.

The final scores for each element in the list then are

```txt
3 3 1
```

Summing these gives a total comfort score for the list of 7.

Your input is a series of lists. For each list, determine the total comfort score of each list, and sum each of these to get the total comfort score of the input, which is your answer.
