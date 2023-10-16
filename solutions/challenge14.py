from collections import defaultdict
from utils import get_file_content


def load_grid(content: str):
    result = {}

    for row_index, line in enumerate(content.splitlines()):
        for column_index, number in enumerate(line.split()):
            result[int(number)] = (row_index, column_index)

    return result


GRID = load_grid('''6  17 34 50 68
10 21 45 53 66
5  25 36 52 69
14 30 33 54 63
15 23 41 51 62''')


def check_numbers(numbers):
    rows = defaultdict(int)
    columns = defaultdict(int)
    diagonal_equal_coordinates = 0
    diagonal_coordinates_equal_to_size = 0

    for index, number in enumerate(numbers):
        if number not in GRID:
            continue

        row, column = GRID[number]
        rows[row] += 1
        columns[column] += 1

        if row == column:
            diagonal_equal_coordinates += 1

        if row + column == 4:
            diagonal_coordinates_equal_to_size += 1

        if (5 in rows.values()) or (5 in columns.values()) or diagonal_equal_coordinates == 5 or diagonal_coordinates_equal_to_size == 5:
            return index + 1

    return 0


def solution(content: str) -> int:
    return sum(map(check_numbers, map(lambda line: map(int, line.split()), content.splitlines())))


assert check_numbers([10, 5, 21, 45, 53, 70, 66, 4]) == 7


print('Solution', solution(get_file_content('input14.txt')))
