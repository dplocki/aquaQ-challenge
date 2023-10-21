from typing import Callable
from utils import get_file_content


def to_second(hour: int, minute: int, second: int) -> int:
    return hour * 60 * 60 + minute * 60 + second


def is_hour_palindromic(hour: int, minute: int, second: int) -> bool:
    if minute % 11 != 0:
        return False

    return (second % 10 == hour // 10) and (second // 10 == hour % 10)


def attach_palindromic_hours(func: Callable) -> Callable:
    palindromic_hours = [
        to_second(hour, minute, second)
        for hour in range(24)
        for minute in range(60)
        for second in range(60)
        if is_hour_palindromic(hour, minute, second)
    ]
    palindromic_hours += [to_second(24, 0, palindromic_hours[0])]

    def inner(time_representation):
        return func(palindromic_hours, time_representation)

    return inner


def str_time_to_seconds(time_representation: str) -> int:
    return to_second(*map(int, time_representation.split(":")))


@attach_palindromic_hours
def find_nearest_palindromic(palindromic_hours: list[int], time_representation: str) -> int:
    requested_time = str_time_to_seconds(time_representation)

    return min(abs(requested_time - hour) for hour in palindromic_hours)


def solution(content: str) -> int:
    return sum(find_nearest_palindromic(line) for line in content.splitlines())


assert solution("13:41:00") == 211

print("Solution", solution(get_file_content("input18.txt")))
