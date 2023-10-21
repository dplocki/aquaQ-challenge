from utils import get_file_content


def is_hour_palindromic(hour: int, minute: int, second: int) -> bool:
    if minute % 11 != 0:
        return False

    return (second % 10 == hour // 10) and (second // 10 == hour % 10)


palindromic_hours = [
    hour * 60 * 60 + minute * 60 + second
    for hour in range(24)
    for minute in range(60)
    for second in range(60)
    if is_hour_palindromic(hour, minute, second)
] + [24 * 60 * 60]


def str_time_to_seconds(time_representation: str) -> int:
    hour, minute, second = map(int, time_representation.split(":"))
    return hour * 60 * 60 + minute * 60 + second


def find_nearest_palindromic(time_representation: str):
    time = str_time_to_seconds(time_representation)

    return min(abs(time - t) for t in palindromic_hours)


assert find_nearest_palindromic("13:41:00") == 211


print(
    "Solution",
    sum(
        find_nearest_palindromic(line)
        for line in get_file_content("input18.txt").splitlines()
    ),
)
