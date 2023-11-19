from typing import Generator, Iterator, List
from utils import get_file_content


def find_extremum(content: str) -> Generator[int, None, None]:
    source = list(map(int, content.split(" ")))

    for index in range(1, len(source) - 1):
        if source[index - 1] < source[index] > source[index + 1]:
            yield source[index]

        elif source[index - 1] > source[index] < source[index + 1]:
            yield source[index]


def take_until(function: callable, iterable: Iterator) -> Generator:
    for i in iterable:
        yield i
        if not function(i):
            return


def prominence(extremum_map: List[int], peak_index: int) -> int:
    def find_prominence(source: Iterator[int]) -> int:
        passed_extremes = list(
            take_until(
                lambda p: p < peak,
                (extremum_map[index] for index in source),
            )
        )

        if passed_extremes and passed_extremes[-1] >= peak:
            return peak - min(passed_extremes)

        return peak

    peak = extremum_map[peak_index]
    left_result = find_prominence(range(peak_index - 1, -1, -1))
    right_result = find_prominence(range(peak_index + 1, len(extremum_map)))

    return min(left_result, right_result)


def solution(content: str) -> int:
    extremum_map = list(find_extremum(content))

    return sum(
        prominence(extremum_map, index) for index in range(0, len(extremum_map), 2)
    )


assert solution("0 1 2 4 6 8 9 8 6 4 2 3 5 6 5 4 5 7 8 6 4 2 1 0") == 17
assert (
    solution(
        "0 1 3 4 6 5 6 5 7 5 6 7 6 4 2 0 1 0 2 4 5 4 3 4 2 4 5 3 5 7 5 7 8 10 11 13 11 9 10 9 7 8 7 8 9 10 8 7 8 6 7 6 4 2 0"
    )
    == 35
)

print("Solution", solution(get_file_content("input40.txt")))
