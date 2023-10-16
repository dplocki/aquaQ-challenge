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


def check_winning(found_number):
    rows = {}
    columns = {}
    diagonal_equal_coordinates = 0
    diagonal_coordinates_equal_to_size = 0

    for row, column in found_number:
        rows[row] = rows.get(row, 0) + 1
        columns[column] = rows.get(column, 0) + 1

        if row == column:
            diagonal_equal_coordinates += 1

        if row + column == 5:
            diagonal_coordinates_equal_to_size += 1

    return (5 in rows.values()) or (5 in columns.values()) or diagonal_equal_coordinates == 5 or diagonal_coordinates_equal_to_size == 5


def check_numbers(numbers):
    found_numbers = set()

    for index, number in enumerate(numbers):
        if number in GRID:
            found_numbers.add(GRID[number])

            if check_winning(found_numbers):
                return index + 1

    return 0


def solution(content: str) -> int:
    return sum(map(check_numbers, map(lambda line: map(int, line.split()), content.splitlines())))


assert check_numbers([10, 5, 21, 45, 53, 70, 66, 4]) == 7


print('Solution', solution(get_file_content('input14.txt')))
