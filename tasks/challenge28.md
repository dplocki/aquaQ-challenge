# Hall of Mirrors

In the continuing series of highly practical methods of encrypting information, we're going to use a hall of rotating "mirrors" to encode basic messages.

The encryption maps used are birds-eye views of a hall of mirrors, like the one below:

```txt
 ABCD
A\  /A
B /\ B
C/ \ C
D/ / D
 ABCD
```

To encrypt, look down the left side for the current letter being encrypted, and start moving right from that letter. Change direction by reflecting from the slashes as if they were mirrors, e.g:

```txt
 /-->
 |
 \-\
   |
->-/
```

After each individual reflection in your path, change the orientation of the mirror you just bounced off - forward slashes become back slashes and vice versa. Follow the path until any letter is reached, which is the encrypted output of the input letter. Then, continue with encryption on the next letter (if any remain) using the map in its current, altered, state.

For example, encrypting the word "DAD" proceeds as below:

```txt
"D"
 Path   Output map
 ABCD      ABCD
A\  /A    A\  /A
B /\ B    B /\ B
C834 C    C/ / C
D765 D    D/ \ D
 ABCD      ABCD

Output: "C" (note position 1 and 7 and position 2 and 8 overlap, before the left turn out of the map)

"A"
 Path   Output map
 ABCD      ABCD
A1  /A    A/  /A
B2/\ B    B /\ B
C3 / C    C\ / C
D/ \ D    D/ \ D
 ABCD      ABCD
Output: "C"

"D"
 Path   Output map
 ABCD      ABCD
A/  /A    A/  /A
B /\ B    B /\ B
C2 / C    C/ / C
D1 \ D    D\ \ D
 ABCD      ABCD
Output: "C"
```

So the final encrypted string in this example is "CCC".

Your map of mirrors is in the input below, use it to encrypt the word "FISSION_MAILED"

The encryted output string is the answer to this challenge.