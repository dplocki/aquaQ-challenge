# Clean Sweep

It's late in the day, and you've just finished a rousing session of AquaQ challenges. Looking at the clock, you realise it's exactly one minute until your spouse gets home, and you promised them you would vacuum the floor, which is currently covered in the debris of a week-long problem-solving session.

You note the hallway floor is covered in a grid of square tiles, and is 20 tiles wide and 500 long. Each tile is covered in a certain amount of dust motes. Quickly you estimate this coverage as relative integers, and note them as your input. Your vacuum cleaner attachment is 5 tiles wide, and for an effective cleaning action, you have to run it so it exactly covers whole tiles. You have time for exactly one pass down the hallway, and can move your vacuum cleaner left or right one tile at a time, or continue straight, as you move forward one tile at a time.

In your single pass down the hallway, starting from any tile on the first row and moving the whole way down, how many motes of dust can you collect, assuming you clean all the dust from each tile?

For an example hallway, with a cleaner width of 3 tiles:

```txt
3 4 5 1 3

9 3 4 0 9

4 5 4 4 7

3 7 9 8 2
```

You can sweep the following tile path to maximise collected motes:

```txt
[3 4 5] 1 3

[9 3 4] 0 9

4 [5 4 4] 7

3 [7 9 8] 2

total: 65
```