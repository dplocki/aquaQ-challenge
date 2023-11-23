# Short walks

You're in an oddly shaped room, there are squares on the floor and you move one square at a time. The room looks like this:

```txt
  ##
 ####
######
######
 ####
  ##
```

This is a six-by-six area defined in indices from 0 to 5 on each axis.
You start in the first # in the top row, or position 0 2 in indices, and recieve a series of instructions to step up (U) left (L) right (R) or down (D) on the map above. You can't step outside the # - if you're given an instruction to do so, ignore it, and move on to the next instruction.

For example, with input UDRR, you eventually run out of instructions at position 1 4.

After processing all the movements in your input, what is the sum of the indices of each position you finished on at each step (including steps where you did not move)?

For example, with input UDRR, you would start on 0 2, stay on 0 2 then move through 1 2, 1 3 and 1 4. The sum of these positions is 14 - the first position is not counted.