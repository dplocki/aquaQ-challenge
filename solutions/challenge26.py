from typing import List
from utils import get_file_content


def index_of_first_higher_than(seek, collection: List) -> int:
    for index, value in enumerate(collection):
        if value > seek:
            return index

    return -1


def rearranged_the_number(number: str) -> int:
    digits = list(number)
    if len(digits) == 1:
        return int(number)

    for index in range(len(digits) - 2, -1, -1):
        sorted_digits_in_part = sorted(digits[index:])

        seek_index = index_of_first_higher_than(digits[index], sorted_digits_in_part)
        if seek_index < 0:
            continue

        sorted_digits_in_part[0], sorted_digits_in_part[seek_index] = (
            sorted_digits_in_part[seek_index],
            sorted_digits_in_part[0],
        )

        return int(
            "".join(
                digits[:index]
                + [sorted_digits_in_part[0]]
                + sorted(sorted_digits_in_part[1:]),
            )
        )

    return int(number)


def solution(raw_content: str) -> int:
    return sum(
        rearranged_the_number(number) - int(number)
        for number in raw_content.splitlines()
    )


assert solution("1423\n121\n10290") == 711

print("Solution:", solution(get_file_content("input26.txt")))
