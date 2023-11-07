from heapq import heappop, heappush
from utils import get_file_content, parse_as_csv_content
from string import ascii_lowercase


def transform_time_to_minutes(time_value: str):
    hour, minutes = map(int, time_value.split(':'))
    return hour * 60 + minutes


def transposition(source):
    result = None
    for row in source:
        if result == None:
            result = [[] for _ in row if _ != 'a']

        tmp = enumerate(row)
        next(tmp)
        for index, column in tmp:
            result[index - 1].append(column)

    yield from result


def transform_to_trains_table(content: str):
    for row in transposition(parse_as_csv_content(content)):
        x = [None if t == '' else transform_time_to_minutes(t) for t in row]

        result = {}
        previous_station = None
        previous_time = 0
        for index, station_time in enumerate(x):
            if station_time == None:
                continue

            station = ascii_lowercase[index]
            result[previous_station] = (station, station_time - previous_time)
            previous_station = station
            previous_time = station_time

        yield result


def solution(content: str) -> int:
    trains = list(transform_to_trains_table(content))

    events = []
    for train_index, train in enumerate(trains):
        heappush(events, (train[None][1], 'arrive', train[None][1], train_index))


    while events:
        event = heappop(events)

    return 0


assert solution('''station,r1,r2,r3
a,00:01,,00:02
b,00:16,,00:17
c,,00:21,
d,00:46,00:51,00:47''') == 64

print('Solution', solution(get_file_content('input34.csv')))
