from typing import List
from utils import get_file_content


def parse(vacuum_size: int, content: str) -> List[List[int]]:
    def transform_line_into_chunks(vacuum_size: int, line: str) -> int:
        numbers = list(map(int, line.split()))
        yield from (
            sum(numbers[index : index + vacuum_size])
            for index in range(len(numbers) - vacuum_size + 1)
        )

    return [
        list(transform_line_into_chunks(vacuum_size, line))
        for line in content.splitlines()
    ]


def find_the_best_path(motes_map: List[List[int]]) -> int:
    size_of_line = len(motes_map[0])
    result = (size_of_line + 2) * [0]

    for motes_line in motes_map:
        new_result = (size_of_line + 2) * [0]

        for index in range(1, size_of_line + 1):
            new_result[index] = (
                max(result[index - 1], result[index], result[index + 1])
                + motes_line[index - 1]
            )

        result = new_result

    return max(result)


def solution(vacuum_size: int, content: str) -> int:
    return find_the_best_path(parse(vacuum_size, content))


assert solution(3, "3 4 5 1 3\n9 3 4 0 9\n4 5 4 4 7\n3 7 9 8 2") == 65
print("Solution", solution(5, get_file_content("input21.txt")))
