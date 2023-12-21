# Brandless Combination Cubes

While solving Rubik's cubes can provide hours of fun, even more fun can be had by mindlessly shuffling them (only to watch them be solved in seconds).

If we start with a numerical version of a Rubik's cube, replacing the colours on each face with numbers, we end up with a cube that looks something like this when flattened out:

```txt
         222
         222
         222
         up (U)

333      111      444
333      111      444
333      111      444
left(L) front(F) right(R)

         555
         555
         555
         down(D)

         666
         666
         666
         back(B)
```


The cube can be manipulated by looking face-on at a side and rotating it either clockwise or anti-clockwise by a quarter-turn around its central point. There is a handy notation for this - a clockwise rotation is the face label (F, L, R, U, D, B) and an anticlockwise rotation is the label followed by an apostrophe (F', L', R', U', D', B').

If we keep the original front face fixed in place, and rotate the faces according to a series of instructions, we can see how the front face of the cube changes:

```txt
input: U'LBRU
U' - rotate the upper face anticlockwise
3 3 3
1 1 1
1 1 1
L - rotate the left face clockwise
2 3 3
2 1 1
2 1 1
B - rotate the back face clockwise (no visible change)
2 3 3
2 1 1
2 1 1
R - rotate the right face clockwise
2 3 5
2 1 5
2 1 3
U - rotate the upper face clockwise
4 4 1
2 1 5
2 1 3

This face has a product like so:
4 x 4 x 1 x 2 x 1 x 5 x 2 x 1 x 3 = 960
```

Starting with the above cube and following the instructions in your input, what is the product of the front face on the cube after executing every rotation in order?
