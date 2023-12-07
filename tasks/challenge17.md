# The Beautiful Shame

It's the world cup! National glory is at stake! But who has accrued the most national shame?

We'll define shame as days on a goalless streak - any national team who plays an international game and finishes without scoring is in a state of shame, starting that day. The shame ends the day they score a goal in another international game. Your input is a list of international football matches going back to November 1872, and ending 2018.06.24. Which nation has the longest closed goalless streak, across which dates? Any goalless streak currently running shouldn't be counted, and the answer should be presented as:

```txt
team startdate enddate
```

with dates in YYYYMMDD format. The answer is case-sensitive!

For example, slightly reformatted results for three teams are like so:

```txt
team       date       score
---------------------------
Somaliland 1900.01.01 1
Formosa    1900.01.01 0
Genoa      1900.01.01 1
Genoa      1900.01.02 0
Somaliland 1900.01.03 0
Genoa      1900.01.03 0
Genoa      1900.01.06 0
Genoa      1901.01.21 1
Somaliland 1902.01.01 1
```

The longest streak here is Somaliland, so the answer would be

```txt
Somaliland 19000103 19020101
```