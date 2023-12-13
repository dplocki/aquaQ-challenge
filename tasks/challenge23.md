# Fair Play

The best way to confound would-be snoops is to use cryptography. Nothing fancy though, they'll be expecting that, so we're using the finest the 1850s has to offer: the Playfair cipher.

This cipher starts with a keyword, which is reduced to the first distinct occurrence of each letter of the alphabet within that word (removing any spaces if necessary). Then all remaining letters of the alphabet (except j) are joined on. The resulting 25 letter string is cut into a 5x5 grid. For example key word "playfair", this results in:

```txt
playf
irbcd
eghkm
noqst
uvwxz
```


The plain text to be encrypted is prepared for lookup in the grid by removing all spaces, splitting repeat letters with "x", padding the string length to the nearest multiple of two (again with "x"), and splitting into two-letter pairs. For example string, "tree":

```txt
tree     //input
trexe    //split double letters
trexex   //pad
tr ex ex //split into bigrams
```

The position of each component of each letter pair is then found in the grid, and encrypted according to the following rules:

1. If the two letters are in the same row, the new letters are the letters directly to the right of the input letters (wrapping around if necessary)
2. If the two letters are in the same column, the new letters are the letters directly below the input letters (wrapping as above)
3. If the letters are separated diagonally, they form the corners of a "box". The encrypted letters are the letters on the laterally opposite end of this box to the input (i.e. look to the far left or right of the input while staying within the box)

For example, if the input text was the word "flawless", this becomes "fl aw le sx sx", which is encoded in the following way:

```txt
"fl" -> "pa"
//on the same row, so the letter to the right
"aw" -> "ba"
//on the same column, so the letter below
"le" -> "pg"
//opposite corners of the square from "l" to "e" in the code square
"sx" -> "xy" (x2)
```

Your input is text encrypted with this method, using the keyword "power plant" - what is the prepared plaintext from this ciphertext? (The answer will contain no "j"s, no spaces, and may be padded with "x"s).
