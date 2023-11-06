from utils import get_file_content


def solution(requested_score: int) -> int:
    points_possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 40, 42, 45, 48, 50, 51, 54, 57, 60]
    cache = [0]

    for score in range(1, requested_score + 1):
        cache.append(min(
            1 + cache[score - points_possibility]
            for points_possibility in points_possibilities
            if score - points_possibility >= 0))

    return sum(cache)


assert solution(30) == 32

print('Solution', solution(int(get_file_content('input33.txt'))))
