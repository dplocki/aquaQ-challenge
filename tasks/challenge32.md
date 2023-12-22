# In Parenthesis

While out shopping, you realise your trousers are falling down - it seems you have forgotten your belt. You realise there are no belt shops in sight, but hope grows when you see a shop whose sign simply reads "Braces".

Upon entering you realise your mistake - this shop simply sells ASCII characters, with a particular emphasis on (, ), [, ], {, and of course }. Desperate to cover your highly embarrassing error, you nod to the shop assistant and shuffle carefully to the ASCII pick-and-mix at the back. You fill up the long thin bags available with individual character strings, and bring them to the counter. The shop assistant looks at your bags, back to you, and back to your bags. He exclaims that surely, surely, you must be joking! Some of these strings have unbalanced braces!

The shame overwhelms you as you slink back to a worktop, and begin examining your hastily-assembled strings more carefully. You realise there are several hundred thousand characters to check, glance back at the assistant twiddling his moustache in delight and begin to wonder if you actually died in that car crash last week.

To weather this existential crisis, in your input set of strings, determine how many lines have brackets (the above set of "()[]{}") which are correctly balanced - that is, the same number of opening and closing pairs, and no pairs which are incorrectly split by other brackets or missing another half.

For example, correctly balanced strings:

```txt
()
([]{})
(a[b[]]c){}
```


Compared to incorrectly balanced strings:

```txt
)()
([a)]
]{}[
((a)){]
```

The answer is the total number of balanced lines in your input - for the above set of 7 rows, the answer would be 3.
