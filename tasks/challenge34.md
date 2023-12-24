After a smashing success at [darts](./challenge33.md), you decide it's time to go home. You live just across the river, but the local ferry only takes coin and you've recently gone cashless, so you decide to take the train. When you get to the station you see a few people milling around, but no-one to help you pick the right train home. The outbound timetables look like the below, with a list of stations and the time each route arrives at that station.

```txt
station r1    r2    r3
-------------------------
a       00:01       00:02
b       00:16       00:17
c             00:21
d       00:46 00:51 00:47
```

So r1 goes to stations a, b, and d. Route r2 goes to c and d only. The station names seem to be set up so that trains always run from lower letters to higher letters.

You notice a sign next to the timetables that reads

```txt
ALL TRAINS MUST NOW REMAIN IN STATION FOR 5 MINUTES
            NO MORE DRIVE-BY PICK UPS
         TIMETABLES DO NOT YET REFLECT THIS
```

You see some other signs as well:

```txt
ONLY ONE TRAIN IN THE STATION AT A TIME
```

```txt
TRAINS FROM LOWER ALPHABETIC STATIONS HAVE QUEUE PRIORITY
            OTHERWISE FIRST IN FIRST OUT
```

```txt
                FOR SAFETY:
    ARRIVE -> QUEUE -> ENTER -> DEPART
```

Clearly you'll have to do some work to determine the real timetable from the one above that doesn't pay attention to train waiting times, the fact that only a single train can be in the station at a time, and the queues that arise from delays. Looking at the structure of the station you realise that trains can queue so they can enter immediately when the previous train leaves the station, but as a sign indicates, they must enter through the queue, and so will be compared to other waiting trains. This means a train arriving from a lower station can sneak in immediately before a queued train from a higher station! Any further ties are broken by route number - e.g. for two trains attempting to originate at station a at the same time on r1 and r2, r1 would enter first. To maintain the idea of ascending alphabetical station order, trains originating at a station can be thought of as coming from the mythical null station, and always have alphabetical priority over a train coming from a named station.

With all this in mind, the above example timetable would play out like so:

```txt
00:01 - r1 enters station a
00:02 - r3 parks outside station a
00:06 - r1 leaves station a for station b, train from r3 enters station a
00:11 - r3 leaves station a for station b
00:21 - r1 arrives at station b, r2 arrives at station c
00:26 - r1 leaves station b for station d, r2 leaves station c for station d, r3 arrives at station b
00:31 - r3 leaves station b for station d
00:56 - r1 and r2 arrive at station d at the same time, r1 gets in first since it arrives from a lower letter station (b)
01:01 - r1 leaves station d completing its journey, r3 arrives at station d and enters immediately as it came from station b
01:06 - r3 leaves station d completing its journey, r2 finally enters station d
01:11 - r2 leaves station d completing its journey
```

So r1 takes 60 minutes to complete its journey, r2 takes 50 minutes, and r3 takes 64 minutes

Your challenge input is an expanded version of a timetable like the one above as a csv file. After running through all the routes, how long does the longest route take in minutes? In this example your answer would be 64.

Note that some of these trains run close to midnight - assume these trains only set off once, and no early runs the next day(s) affect your currently running trains.
