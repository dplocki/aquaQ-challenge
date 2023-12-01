# Boxed In

You've been presented with the plans for an avant-garde method of tiling floors. You have a list of values which represent the lower-left and upper-right corner co-ordinates of a series of rectangular tiled areas, where one tile is equal to one square unit.

The designer then specifies that he doesn't want any areas that don't overlap others included in the final plan - if an area doesn't directly overlap with another, disregard it entirely. In the resulting set of areas, some tiles overlap - since there's no point in placing more than one tile per spot, so how many tiles do you need total to complete the plan?

For example, if you were provided with these three tiled areas:

```csv
lx,ly,ux,uy
0,0,3,3
2,2,4,5
6,3,8,7
```

The direct map would look like this, with (0,0) in the bottom left corner:

```txt
      ##
      ##
  ##  ##
  ##  ##
##@#
###
###
```

There is an overlap of two tiles in the square bounded by (2,2) and (3,3), and the tiles at the top right are not connected to any other tiles. In this case the total number of required tiles is 14.
