from typing import Generator, Iterator, Tuple
from utils import get_file_content


def get_winning_darts_in_leg(
    source_darts: Iterator[int],
) -> Generator[Tuple[str, int], None, None]:
    score = {"A": 0, "B": 0}
    streak = 0

    player_starting_leg = "A"
    current_player = player_starting_leg
    for dart in source_darts:
        if streak >= 3:
            streak = 0
            current_player = "B" if current_player == "A" else "A"

        score[current_player] += dart
        streak += 1

        if score[current_player] >= 501:
            yield current_player, dart

            score["A"] = 0
            score["B"] = 0
            streak = 0
            player_starting_leg = "B" if player_starting_leg == "A" else "A"
            current_player = player_starting_leg


def solution(content: str) -> int:
    how_many_wins = 0
    sum_winning_darts = 0

    for player, dart in get_winning_darts_in_leg(map(int, content.split(" "))):
        if player == "A":
            how_many_wins += 1

        sum_winning_darts += dart

    return how_many_wins * sum_winning_darts


assert (
    solution(
        "11 38 9 25 24 15 50 10 8 40 17 24 10 6 10 38 6 12 32 19 16 18 16 51 39 34 24 4 54 9 6 32 51 11 1 30 3 12 40 32 9 14 2 3 36 12 60 42 33 1 6 45 36 5 21 57 4 51 30 11 7 36 20 24 14 28 54 17 18 12 18 36 10 38 16 18 7 27 12 34 40 9 16 25 22 15 15 20 8 12 13 16 4 57 39 11 13 40 5 33 36 36 1 54 45 19 3 18 30 57 5 3 8 9 40 3 40 9 17 60 26"
    )
    == 156
)

print("Solution", solution(get_file_content("input39.txt")))
