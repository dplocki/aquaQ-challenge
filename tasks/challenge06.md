# Let me count the ways

It can be useful to know how to break down a number - usually this is done with factors, but instead, let's try it with summable components. For a number, you can work out the possible combinations of non-negative integers which sum to that number. For example, these are the combinations of three numbers which sum to 3:

```txt
0 0 3
0 1 2
0 2 1
0 3 0
1 0 2
1 1 1
1 2 0
2 0 1
2 1 0
3 0 0
```

The digit "1" occurs 9 times above. For your input, how many times does the character "1" appear in all combinations summing to that number?

Note the number "11" would be twice, "21" once, so 1 21 11 would be 4 times.
