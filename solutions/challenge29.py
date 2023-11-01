from math import floor, log10
from utils import get_file_content


def solution(maximum_number: int) -> int:
    cache = {(i * 10): (10 - i) for i in range(10)}

    multiplayer = 100
    while multiplayer < maximum_number:
        for i in range(1, 10):
            cache[i * multiplayer] = sum(
                cache[j * multiplayer // 10] for j in range(i, 10)
            )

        multiplayer *= 10

    limes = maximum_number - 10 ** floor(log10(maximum_number))

    return sum(value for key, value in cache.items() if key <= limes)


print("Solution", solution(int(get_file_content("input29.txt"))))
