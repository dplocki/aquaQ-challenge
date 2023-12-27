# Columns

Wandering around the train station, waiting for [several decades of timetable backlog to clear](./challenge34.md), you find some books on a table. The perfect way to pass the time! Picking up the first book you see what looks like a jumble of letters, instead of a story. In fact, all the books look like this, and there are no titles on the covers either. Someone has left a note next to the books, mercifully in plain text:
"These are encrypted with a columnar transposition cipher".

Cryptic but useful. Since you have so much time, you decide to work through decrypting these books, but you're missing one particular piece of information - the code word. You think back to what you know on columnar transposition ciphers.

To make a columnar transposition cipher, take a body of text:

```txt
WE ARE DISCOVERED FLEE AT ONCE
```

and a code-word:

```txt
GLASS
```

Chop the text into lengths equal to the length of the code word (5 letters, in this case), padding the end of the plaintext if necessary:

```txt
WE AR
E DIS
COVER
ED FL
EE AT
 ONCE
```

(Note that usually spaces and punctuation would be removed, but since we want to recover the original plaintext of the book in full, we won't do that here)

Then use the code word to generate a selection order for the columns. The selection order is the order the letters in the word would take if they were sorted alphabetically.
For example

```txt
G L A S S
```

becomes

```txt
1 2 0 3 4
```

as A is the first alphabetical letter, G the second, L the third and S is both the fourth and fifth. Ties are broken by position in the original word, so

```txt
L E V E R
```

becomes

```txt
2 0 4 1 3
```


since both Es can't be 0, the second E becomes 1. A third E would become 2 and all other letters would increase by one, etc.

Taking this column order, apply to the columns:

```txt
12034
WE AR
E DIS
COVER
ED FL
EE AT
 ONCE
```


And pull the columns out in that order, converting to lines:

```txt
 DV  N
WECEE
E ODEO
AIEFAC
RSRLTE
```


And then collapse into a single string:

```txt
 DV  NWECEE E ODEOAIEFACRSRLTE
```

Your input is a section from one of the books, as a ciphertext (a "#" has been added to the end of this to note the end position of the ciphertext - feel free to remove it). You have a [handy list of words here](./words.txt), which will contain the code word. What is the code word used to encrypt the text in your input?