from functools import reduce
from operator import mul

from utils import get_file_content


def solution(lines: str) -> int:
    return reduce(mul, map(int, lines.splitlines()))

assert solution('''2
4
8''') == 64

print('Solution', solution(get_file_content('input09.txt')))
