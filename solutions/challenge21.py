from typing import List
from utils import get_file_content


def transform_line_into_chunks(vacuum_size: int, line: str) -> int:
    a = list(map(int, line.split()))
    yield from (sum(a[i : i + vacuum_size]) for i in range(len(a) - vacuum_size + 1))


def parse(vacuum_size: int, content: str) -> List[List[int]]:
    return [
        list(transform_line_into_chunks(vacuum_size, line))
        for line in content.splitlines()
    ]


def find_the_best_path(vacuum_size: int, motes_map: List[List[int]]) -> int:
    size_of_line = len(motes_map[0])
    result = (size_of_line + 2) * [0]

    for motes_line in motes_map:
        new_result = (size_of_line + 2) * [0]

        for i in range(1, size_of_line + 1):
            new_result[i] = (
                max(result[i - 1], result[i], result[i + 1]) + motes_line[i - 1]
            )

        result = new_result

    return max(result)


def solution(vacuum_size: int, content: str) -> int:
    return find_the_best_path(vacuum_size, parse(vacuum_size, content))


assert solution(3, "3 4 5 1 3\n9 3 4 0 9\n4 5 4 4 7\n3 7 9 8 2") == 65
print("Solution", solution(5, get_file_content("input21.txt")))
