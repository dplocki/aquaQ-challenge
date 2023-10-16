from collections import defaultdict
from utils import get_file_content


def load_grid(content: str):
    return {
        int(number): (row_index, column_index)
        for row_index, line in enumerate(content.splitlines())
        for column_index, number in enumerate(line.split())
    }


GRID_SIZE = 5
GRID = load_grid(
    """6  17 34 50 68
10 21 45 53 66
5  25 36 52 69
14 30 33 54 63
15 23 41 51 62"""
)


def check_numbers(grid_size, grid, numbers):
    rows = defaultdict(int)
    columns = defaultdict(int)
    diagonal_equal_coordinates = 0
    diagonal_coordinates_equal_to_size = 0

    for index, number in enumerate(numbers):
        if number not in grid:
            continue

        row, column = grid[number]
        rows[row] += 1
        columns[column] += 1

        if row == column:
            diagonal_equal_coordinates += 1

        if row + column + 1 == grid_size:
            diagonal_coordinates_equal_to_size += 1

        if (
            (grid_size in rows.values())
            or (grid_size in columns.values())
            or diagonal_equal_coordinates == grid_size
            or diagonal_coordinates_equal_to_size == grid_size
        ):
            return index + 1

    return 0


def solution(content: str) -> int:
    return sum(
        map(
            lambda numbers: check_numbers(GRID_SIZE, GRID, numbers),
            map(lambda line: map(int, line.split()), content.splitlines()),
        )
    )


assert check_numbers(GRID_SIZE, GRID, [10, 5, 21, 45, 53, 70, 66, 4]) == 7

print("Solution", solution(get_file_content("input14.txt")))
