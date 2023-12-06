# Keming

Nothing is more exciting than a bracing bout of typography.

Like most people, I am commonly unable to sleep because of the knowledge that some letters around me are poorly spaced. Today, this problem will be remedied for the equally-common occurence of ascii art words. An alphabet of these words is found [here](./asciialphabet.txt).

Kerning is the process of correctly spacing letter pairs to make use of the white-space surrounding each letter. For example, if I was joining the letters L and T together from the above alphabet and putting a space between them, without kerning, it would look like this:

```txt
#..... #####
#........#..
#........#..
#........#..
#........#..
######...#..
```

All that wasted space between the top of the L and the top of the T is frankly offensive. The rule that should be used to join these together is to move the letters closer together until the nearest horizontal points between them are separated by a single space (filled with dots in this case to show spacing). For example, the L and T following this rule would look like:

```txt
#....#####
#......#..
#......#..
#......#..
#......#..
######.#..
```

The T has been moved closer to the L until there is only one space between them at the closest point, and there is no overlap.

After drawing a box around this resulting combination of letters which just encompasses all the "#", we can see there are 51 spaces before applying kerning, and 39 after. Subsequent letters would be joined onto this "LT" combination in exactly the same way, following the single-space rule, and treating the LT as a single character - for example "LTA" would use some of the space under the right edge of the T, and would end up looking like:

```txt
#....#####.##..
#......#..#..#.
#......#.#....#
#......#.######
#......#.#....#
######.#.#....#
```

Using a total of 53 spaces.

Convert your input string into the appropriate ASCII characters in the above link, and join them together while applying the kerning rule - what is the total number of empty spaces in the resulting set of strings?
