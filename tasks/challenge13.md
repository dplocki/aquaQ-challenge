# O RLE?

Run Length Encoding is a basic form of lossless compression - an array of data, or a subset of the array, can be converted into a smaller subset (a run) which repeats some number of times (a length). For example:

```txt
"ABCABCABCABCABC"
```

could become:

```txt
5 "ABC"
```

Here, 15 characters have been converted into an integer and 3 characters.

Your input contains a list of strings - they each contain a repeated sequence like the one above, however there are some extra characters on the beginning and end. Once these characters have been removed, what is the sum of the counts of the most repeated blocks in each string?

For example:

```txt
"AAAAAAB"
```

could be broken down into 2 counts of "AAA", 3 counts of "AA" or 6 counts of "A" - thus "A" is the most-repeated block and the answer for this string is 6. If your entire input consisted of two copies of this string, the challenge answer would be 12.
