# Snake Eater

Word snakes, while not as cool as their reptilian counterparts, are still undoubtedly the coolest way to represent a string of words, right?

They look like this:

```txt
                roulette
                e      l
                v      e
                e      c
                netulg t
    invalidly        n i
            a        i o
            c        y n
            h        r sharpness
            t        r
            i        u
            n        c
            grumpiness
```

In case you disagree re: the aforementioned coolness, the words used in this word snake are:

```txt
invalidly
yachting
grumpiness
scurrying
gluten
never
roulette
elections
sharpness
```

To find the answer to this challenge, take this disgreement to the next level and find all the words in the snakes in your challenge input. Once the words have been found, your answer is the sum of the value of each of the words. The value of a word is found by getting the letter values of that word (a=1, b=2, etc), summing them, and multiplying by the count of letters in the word.

For the above snake, the answer would be 7995. There is more than one snake in your input - the answer is the sum of all values of all words.
