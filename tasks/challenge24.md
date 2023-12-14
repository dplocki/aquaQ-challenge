# Huff and Puff

Huffman coding is a method of data compression, converting fixed-length items in memory into variable length items. We're using it here to convert letters into bits. The conversion ensures no two output codes share the same prefix, since this can lead to ambiguity when the compressed outputs are run together. For example converting "aba":

```txt
Good:
  a -> 011
  b -> 101
  output: 011101011

Bad:
  a -> 110
  b -> 1
  c -> 0
  output:110110
```

In the second case, you have no idea where codes end or begin. In the first, it's unambiguous - as soon as you have passed 011 in the input, you have an "a", then the 101 gives "b" etc.

To construct a Huffman code, the text to be converted is reduced to the frequency of its characters. We'll use the wikipedia example text:

```txt
A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED
```

The frequency of each character is then:

```txt
C:2
B:6
E:7
D:10
_:10
A:11
```

In this initial frequency listing, ties are broken by ASCII code order. This could be seen as a tree where every element is an unconnected node with a weight determined by the frequency.

The first two elements at each point are merged together into a single node with two direct subnodes - the elements are placed side-by-side (whether full tree or single node) and both are connected directly to a shared parent node above. This new tree has a total weight of the sum of all letters in it. The tree is then re-inserted into the above set of nodes, and the set sorted based on the total weight of each node and its subnodes. In the case of a tie, new trees are inserted at the bottom of the group of their tied weights (e.g. a group "ab" with weight 10 would go into a node group "c:7 f:10 g:10 l:11" after the "g)"

Converting the above into a tree, with nodes and their weight, this looks like:

```txt
E:7  CB:8  D:10  _:10  A:11
     /  \
   C:2  B:6
```


This same approach is applied again, where the newly created node is now the highest value, and so is joined at the end:

```txt
D:10  _:10  A:11  ECB:15
                  /   \
               E:7   CB:8
                     /  \
                   C:2  B:6
```


This process of joining the first two and reinserting is continued until the tree looks like:

```txt
      D_AECB:46
     /         \
  D_:20       AECB:26
  /   \        /    \
D:10  _:10   A:11  ECB:15
                   /   \
                 E:7  CB:8
                      /  \
                    C:2  B:6
```

To get the final codes from this tree, the desired letter is travelled to and the left-right pattern is converted to 0 and 1. For example, "e" requires travelling right-right-left from the topmost node, which becomes 110, while d is left-left, or 00.
The final code is then:

```txt
D:00
_:01
A:10
E:110
C:1110
B:1111
```

And so encoded, the word "CEDED" becomes:
11101100011000

The input to this puzzle is in two parts - the first line is a set of characters. Use these characters to follow the above rules to build the tree and obtain the Huffman code for each letter.

The second line contains the answer to the challenge as Huffman coded bits, which should be decoded and entered below.