from typing import Generator, Iterator, Tuple
from utils import parse_as_csv_content, get_file_content
from datetime import date


def parse_wrapper(
    source: Iterator[Tuple],
) -> Generator[Tuple[str, int, str, int], None, None]:
    for (
        match_date,
        home_team,
        away_team,
        home_score,
        away_score,
        _,
        _,
        _,
        _,
    ) in source:
        yield date.fromisoformat(match_date), home_team, int(home_score)
        yield date.fromisoformat(match_date), away_team, int(away_score)


def get_shameful_strick(source: Iterator[Tuple]):
    memory = {}

    for date, team, score in parse_wrapper(source):
        if score != 0 and team in memory:
            yield abs((memory[team] - date).days), team, memory[team], date
            del memory[team]
        elif score == 0 and team not in memory:
            memory[team] = date


def solution(content: str) -> str:
    s = 0
    p = None

    for i in get_shameful_strick(parse_as_csv_content(content)):
        if i[0] > s:
            p = i
            s = i[0]

    return f'{p[1]} {date.strftime(p[2], "%Y%m%d")} {date.strftime(p[3], "%Y%m%d")}'


print("Solution:", solution(get_file_content("input17.csv")))
