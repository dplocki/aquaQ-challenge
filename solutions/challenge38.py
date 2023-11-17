from typing import Generator, Iterator, List
from utils import get_file_content


def parsing(content: str) -> Generator[Iterator[int], None, None]:
    for line in content.splitlines():
        yield map(int, line.split())


def find_streak(numbers: List[int], index: int, current_streak_length: int) -> bool:
    for start in range(index - current_streak_length + 1, index + 1):
        if start < 0 or start + current_streak_length > len(numbers):
            continue

        if (
            sum(numbers[start + i] for i in range(current_streak_length))
            % current_streak_length
            == 0
        ):
            return True

    return False


def find_the_longest_streak(numbers: List[int], index: int, max_streak: int) -> int:
    for current_streak_length in range(2, max_streak + 1):
        if not find_streak(numbers, index, current_streak_length):
            return current_streak_length - 1

    return max_streak


def comfortable(numbers: List[int]) -> int:
    max_streak = len(numbers)
    return sum(
        find_the_longest_streak(numbers, index, max_streak)
        for index in range(max_streak)
    )


def solution(content: str) -> int:
    return sum(comfortable(list(numbers)) for numbers in parsing(content))


assert comfortable([1, 3, 2]) == 7

print("Solution", solution(get_file_content("input38.txt")))
