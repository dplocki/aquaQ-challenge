# One is all you need

You've found a table which is supposed to record only unique values in the order they appeared. Looking closely, you realise that some of the values occur multiple times. Consulting the documentation, you see the original system was designed to only have data appended, so there was no way to correct broken inputs.

Instead, a record appearing more than once means that everything between the first instance of that record up to the latest occurrence was incorrect, and should be discarded. Values after this occurrence are treated as if those records in between hadn't existed. What is the sum of the values returned from your input after this process has been applied?

For example input:

```txt
1 4 3 2 4 7 2 6 3 6

f[1 4 3 2 4 7 2 6 3 6]
1 4 7 2 6
```

In this case, the summed answer would be 20.
