from typing import Generator

from utils import get_file_content


def prime_factors(n: int) -> Generator[int, None, None]:
    while n % 2 == 0:
        yield 2
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            yield i
            n = n // i

    if n > 2:
        yield n


def is_factor(primes: [int], n: int) -> int:
    for p in primes:
        if n % p == 0:
            return True

    return False


def solution(n: int) -> int:
    primes = list(prime_factors(n))

    return sum(m for m in range(1, n) if not is_factor(primes, m))


assert solution(15) == 60

print("Solution", solution(int(get_file_content("input04.txt"))))
