import math
from utils import get_file_content


def first_true(pred, iterable):
    return next(filter(pred, iterable))


def number_to_roman(value: int) -> str:
    result = ''

    if value >= 1000:
        result += (value // 1000) * 'M'
        value -= 1000 * (value // 1000)

    if value // 100 == 9:
        value -= 900
        result += 'CM'

    if value // 100 >= 5:
        value -= 500
        result += 'D'

    if value // 100 == 4:
        value -= 400
        result += 'CD'

    if value >= 100:
        result += (value // 100) * 'C'
        value -= 100 * (value // 100)

    if value // 10 == 9:
        value -= 90
        result += 'XC'

    if value // 10 == 4:
        value -= 40
        result += 'XL'

    if value // 10 >= 5:
        value -= 50
        result += 'L'

    if value >= 10:
        result += (value // 10) * 'X'
        value -= 10 * (value // 10)

    if value == 9:
        result += 'IX'
        value -= 9

    if value >= 5:
        result += 'V'
        value -= 5

    if value == 4:
        result += 'IV'
        value -= 4

    result += (value % 10) * 'I'

    return result


def str_to_numeric_value(value: str) -> int:
    letter_a = ord('A')

    return sum(
        ord(character) - letter_a + 1
        for character in value)


def solution(content: str):
    return sum(map(str_to_numeric_value, map(number_to_roman, map(int, content.split()))))


print('Solution', solution(get_file_content('input22.txt')))
