from typing import Dict, Tuple
from utils import get_file_content, parse_as_csv_content
from string import ascii_lowercase

WAITING_ON_STATION_MINUTES = 5
TRAIN_SOURCE = "_"


class Train:
    def __init__(self, name: str, time_table: Dict[str, Tuple[str, int]]) -> None:
        self.name = name
        self.time_table = time_table
        self.previous_station = TRAIN_SOURCE


class TrainBuilder:
    def __init__(self, name: str) -> None:
        self.name = name
        self.last_station = TRAIN_SOURCE
        self.last_station_time = 0
        self.time_table = {}

    def add_station(self, station_name: str, time_arrival: int) -> None:
        self.time_table[self.last_station] = (
            station_name,
            time_arrival - self.last_station_time,
        )
        self.last_station = station_name
        self.last_station_time = time_arrival

    def build_run(self):
        return Train(self.name, self.time_table)


def transform_time_to_minutes(time_value: str):
    hour, minutes = map(int, time_value.split(":"))
    return hour * 60 + minutes


def transform_to_trains_table(content: str):
    timetable_content = parse_as_csv_content(content, skip_headers=False)

    headers = next(timetable_content)

    trains_builders = [TrainBuilder(name) for name in headers[1:]]

    for row in timetable_content:
        station_name = row[0]

        for time_arrival, trains_builder in zip(row[1:], trains_builders):
            if time_arrival == "":
                continue

            trains_builder.add_station(
                station_name, transform_time_to_minutes(time_arrival)
            )

    return [tb.build_run() for tb in trains_builders]


def solution(content: str) -> int:
    trains = transform_to_trains_table(content)

    return


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
