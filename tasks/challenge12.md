# A Day In The Lift

Your childhood dream has been fulfilled: you are a lift in the world's tallest building. Your instructions come in a series of number pairs for each floor. The first number indicates whether you should continue in the same direction (1) or immediately reverse direction (0).

After this is decided, the second number indicates how many floors you should immediately move by. You continue in the same direction until you see a zero instruction in the first number. Your working day is over when you land on a floor without instructions.

For example, if you had the instruction set:

```txt
1 2   //0
0 3   //1
1 1   //2
0 1   //3
1 5   //4
```

Starting at floor 0, you would move 2 floors up to floor 2, then 1 floor to floor 3, and immediately reverse direction. Then move 1 floor back to floor 2, then 1 more back to floor 1, at which point you reverse direction again, moving to floor 4, which sends you to floor 9 - which has no instructions. Your work is then done, and you'll have visited 7 floors - 0, 1, 2 (twice), 3, 4 and 9.

How many floors do you visit before finishing when following your input instructions?