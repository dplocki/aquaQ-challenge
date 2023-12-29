# GUESS WORDS

You decide to relax with some nice, simple word games. Recently, you have heard of [a game which is sweeping the globe, consuming all in its path](https://www.powerlanguage.co.uk/wordle/). You decide to slay this beast.

The game is played by guessing the letters of five-letter words. Each time you input a word, you are told which of the five letters are correct and in the correct location, and which are wrong, and in the wrong location. You quickly solve several of these by hand, forming a table of guesses and results like so:

```txt
guess   result
-----------------
"guess" 0 0 0 0 2
"twins" 0 1 0 0 2
"bowls" 0 2 1 0 2
"worms" 2 2 2 0 2
"works" 2 2 2 0 2
```

At each guess, you mark down a 0 for a totally incorrect letter, a 1 for a correct letter in the wrong place, and a 2 for a correct letter in the correct place. After working through the guesses above, you realise the only possible word it can be is WORDS. As you look at all of your guesses you realise, in fact, that you haven't recorded any of these answer words at all!

Your input looks like a long version of the table above. Every time you identify a single answer word, you start a new set of guesses with a new, unknown answer. In the above example, the next guess might be WILDS, and the result might be 0 2 0 0 0, because a new word is the "correct" answer, and the correct answer WORDS is never written down. Answers are in the subset of five letter words contained [here](./words.txt).

Using your input, retrieve all of the correct answer words, convert the letters in each answer word to numbers (A = 0, B = 1, C = 2, etc), and sum them.
For example the unique word above is WORDS. If another set of answers gave us MINCE as well, the final answer would be 113.
