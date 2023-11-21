# What's a numpad?

Some people might remember T9 phone inputs, in which the numbers 2 to 9 have associated letters, and 0 acts as a space. Key 2 has "abc", 3 has "def" etc:

```txt
  1   2   3
     abc def

  4   5   6
 ghi jkl mno

  7   8   9
pqrs tuv wxyz
     
      0
      _
```

Note that 0 is a space, not an underscore!

To get a letter you press the button a certain number of times - pressing 2 once gives "a", twice gives "b".
The input is a list of number pairs: a key and the number of times it has been pressed. For example, "7 3" would be "r". What is the message this input produces?
