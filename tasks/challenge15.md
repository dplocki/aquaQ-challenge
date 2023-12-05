# word wore more mare maze

As a child, nothing is more difficult and mysterious than the game which apparently has no name, but goes like this:

You have a starting word, and an ending word - changing one letter at a time and always maintaining a real word, make a chain of words from the start to the end. For example:

```txt
fly
...
try
```

Results in

```txt
fly
fry
try
```

This results in a chain three words long, including the starting and ending words.

Using the word list here as a list of valid words, find the shortest full chain of each word pair in the input. The answer is the product of the lengths of each chain - so if the input was

```txt
fly,try
try,fly
word,maze
```

The lengths of each chain would be 3 3 5, and the product of these would be the answer: 45.