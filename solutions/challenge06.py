from utils import get_file_content


def find_combination_of_sum(n: int):
    for first in range(n + 1):
        for second in range(n - first + 1):
            yield first, second, n - first - second


def solution(n: int) -> int:
    result = 0
    for item in find_combination_of_sum(n):
        result += str(item).count('1')

    return result


def get_number_from_input(text: str) -> int:
    return int(text.split(' ')[-1])


assert solution(3) == 9

print('Solution', solution(get_number_from_input(get_file_content('input06.txt'))))
