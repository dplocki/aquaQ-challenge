# Troll Toll

A new bitcoin fork has taken over! In this new system, users can use a modified form of the [lightning network](https://en.wikipedia.org/wiki/Lightning_Network), in which users are connected to some subset of other users, and can freely transfer money to each other. In this system, transferring money directly between users costs some small amount of pence - a different amount from user to user.

A set of user source-destination pairs and the cost to transfer between them looks like this:

```txt
 s  d  c
 --------
 A  B  8
 B  C  50
 B  D  5
 D  E  10
 E  C  6
```

Mapped out, with the costs between the users, this would look like:


```txt
 A--8--B--50--C
       |      |
       5      6
       |      |
       D--10--E
```

If user A wants to send money to user C, they can send via route ABC, costing 58p, or ABDEC, costing 29p.

In your input, you have a number of user pairs (listed in both directions) and their costs. Tupac owes Diddy fifty pounds - what's the smallest extra amount he'll have to spend (in pence) to pay back Diddy this fiddy?
