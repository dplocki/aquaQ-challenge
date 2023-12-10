# Blackjack

Imagine the thrill of the casino, right there in your terminal.

Magnificent.

Today, we're playing the most sedate games of not-quite-blackjack of which you could concieve. Your input is a set of decks of cards, shuffled together. Draw from this deck, in order, one card at a time. Any time you hit a total card value of 21, you win! Any time you go over 21 you lose. In either case, once a game is done, immediately start again with the next card, and repeat until there are no cards left.

It's important to note while playing you can consider aces to be 11 or 1 at any time, while 2 to 10 have their face value and Jack, Queen and King are worth 10.

An example play is below

```txt
input: 3 A K 9 A 7 4 9
Draw a 3: current total 3
Draw an ace: current total 4 or 14
Draw a King: current total 14 or 24
Draw a 9: current total 23 or 33
This is a loss. Start again with the next card:
Draw an ace: current total 1 or 11
Draw a 7: current total 8 or 18
Draw a 4: current total 12 or 22
Draw a 9: current total 21 or 31
This is a win!
```

So for this input, you win one game. How many games do you win with the input for this challenge?