from typing import Generator, Iterator, Tuple
from utils import get_file_content, parse_as_csv_content


def parse_wrapper(
    source: Iterator[Tuple],
) -> Generator[Tuple[str, int, str, int], None, None]:
    for first_player, second_player, score in source:
        first_player_points, second_player_points = map(int, score.split("-"))
        yield first_player, first_player_points, second_player, second_player_points


def calculate_rate(ra: float, rb: float) -> float:
    return 1 / (1 + 10 ** ((rb - ra) / 400))


def update_rating(rate: float) -> float:
    return 20 * (1 - rate)


def run_make(content: str) -> dict[str, int]:
    score_table = {}

    for (
        first_player,
        first_player_points,
        second_player,
        second_player_points,
    ) in parse_wrapper(parse_as_csv_content(content)):

        ra = score_table.get(first_player, 1200)
        rb = score_table.get(second_player, 1200)

        if first_player_points > second_player_points:
            rate = calculate_rate(ra, rb)
            score_table[first_player] = ra + update_rating(rate)
            score_table[second_player] = rb - update_rating(rate)
        else:
            rate = calculate_rate(rb, ra)
            score_table[first_player] = ra - update_rating(rate)
            score_table[second_player] = rb + update_rating(rate)

    return score_table


def solution(file_name: str) -> int:
    score_table = run_make(file_name)

    scores = score_table.values()

    return int(max(scores)) - int(min(scores))


print("Solution", solution(get_file_content("input07.csv")))
