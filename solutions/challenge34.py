from heapq import heappop, heappush
from utils import get_file_content, parse_as_csv_content
from string import ascii_lowercase

WAITING_ON_STATION = 5
TRAIN_SOURCE = "_"


def transform_time_to_minutes(time_value: str):
    hour, minutes = map(int, time_value.split(":"))
    return hour * 60 + minutes


def transposition(source):
    result = None
    for row in source:
        if result == None:
            result = [[] for _ in row if _ != "a"]

        tmp = enumerate(row)
        next(tmp)
        for index, column in tmp:
            result[index - 1].append(column)

    yield from result


def transform_to_trains_table(content: str):
    for row in transposition(parse_as_csv_content(content)):
        x = [None if t == "" else transform_time_to_minutes(t) for t in row]

        result = {}
        previous_station = TRAIN_SOURCE
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
    stations_names = set()
    trains = []

    for s in transform_to_trains_table(content):
        trains.append(s)
        stations_names.update(s.keys())
        stations_names.update(x[0] for x in s.values())

    stations_names.remove(TRAIN_SOURCE)
    events = []
    starts_times = {}
    ends_times = {}

    stations_queues = {s: [] for s in stations_names}
    stations = {s: None for s in stations_names}

    for train_index, train in enumerate(trains):
        starts_times[train_index] = train[TRAIN_SOURCE][1]
        heappush(
            events,
            (
                train[TRAIN_SOURCE][1],
                "arrive",
                train_index,
                train[TRAIN_SOURCE][0],
                TRAIN_SOURCE,
            ),
        )

    while events:
        time, event_type, train_index, current_station, from_station = heappop(events)

        if event_type == "arrive":
            if stations[current_station] == None:
                stations[current_station] = train_index
                heappush(
                    events,
                    (
                        time + WAITING_ON_STATION,
                        "leave",
                        train_index,
                        current_station,
                        current_station,
                    ),
                )
            else:
                stations_queues[current_station].append((from_station, train_index))
        elif event_type == "leave":
            stations[current_station] = None
            if stations_queues[current_station]:
                stations_queues[current_station].sort(key=lambda q: q[0], reverse=True)
                train_id = stations_queues[current_station].pop()[1]
                stations[current_station] = train_id
                heappush(
                    events,
                    (
                        time + WAITING_ON_STATION,
                        "leave",
                        train_id,
                        current_station,
                        current_station,
                    ),
                )

            if current_station not in trains[train_index]:
                ends_times[train_index] = time
            else:
                to_state, time_difference = trains[train_index][current_station]
                heappush(
                    events,
                    (
                        time + time_difference,
                        "arrive",
                        train_index,
                        to_state,
                        current_station,
                    ),
                )

    return max(ends_times[train_index] - _from for train_index, _from in starts_times.items())


assert (
    solution(
        """station,r1,r2,r3
a,00:01,,00:02
b,00:16,,00:17
c,,00:21,
d,00:46,00:51,00:47"""
    )
    == 64
)

print("Solution", solution(get_file_content("input34.csv")))
