from typing import Dict, Generator, Set, Tuple
from utils import get_file_raw_content


def get_neighbors(x: int, y: int) -> Generator[Tuple[int, int], None, None]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def parse_content_to_map(content: str) -> Dict[Tuple[int, int], str]:
    result = {}

    for row_index, row in enumerate(content.splitlines()):
        for column_index, column in enumerate(row):
            if column != " ":
                result[row_index, column_index] = column

    return result


def find_snake_endings(
    _map: Dict[Tuple[int, int], str]
) -> Generator[Tuple[int, int], None, None]:
    for row, column in _map:
        neighbor = [(r, c) for r, c in get_neighbors(row, column) if (r, c) in _map]

        if len(neighbor) == 1:
            yield row, column


def only_valid_neighbors(
    _map: Dict[Tuple[int, int], str], point: Tuple[int, int]
) -> Generator[Tuple[int, int], None, None]:
    yield from (p for p in get_neighbors(*point) if p in _map)


def walk(
    was: Set[Tuple[int, int]],
    _map: Dict[Tuple[int, int], str],
    start_point: Tuple[int, int],
) -> Generator[str, None, None]:
    if start_point in was:
        return

    next_point = next(only_valid_neighbors(_map, start_point))
    direction = next_point[0] - start_point[0], next_point[1] - start_point[1]
    current_point = start_point

    result = ""

    while True:
        result += _map[current_point]
        was.add(current_point)
        new_current_point = (
            current_point[0] + direction[0],
            current_point[1] + direction[1],
        )

        if new_current_point not in _map:
            neighbors = [
                n for n in only_valid_neighbors(_map, current_point) if n not in was
            ]
            if len(neighbors) == 0:
                yield result
                return

            next_point = neighbors[0]
            direction = (
                next_point[0] - current_point[0],
                next_point[1] - current_point[1],
            )

            yield result
            result = ""
        else:
            current_point = new_current_point


def solution(content: str) -> int:
    _map = parse_content_to_map(content)
    letter_a = ord("a")
    was = set()

    return sum(
        sum(ord(letter) - letter_a + 1 for letter in word) * len(word)
        for start in sorted(
            find_snake_endings(_map), key=lambda coordinates: coordinates[1]
        )
        for word in walk(was, _map, start)
    )


test_input = """                roulette
                e      l
                v      e
                e      c
                netulg t
    invalidly        n i
            a        i o
            c        y n
            h        r sharpness
            t        r
            i        u
            n        c
            grumpiness"""

assert solution(test_input) == 7995

print("Solution", solution(get_file_raw_content("input27.txt")))
