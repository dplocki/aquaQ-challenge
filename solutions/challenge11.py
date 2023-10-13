from itertools import combinations, product
from utils import parse_as_csv_content, get_file_content


def parse_wrapper(source):
    yield from (list(map(int, line)) for line in source)


def solution(content: str) -> int:
    areas = [
        set(product(range(lower_x, upper_x), range(lower_y, upper_y)))
        for lower_x, lower_y, upper_x, upper_y in parse_wrapper(
            parse_as_csv_content(content)
        )
    ]

    result = set()
    for area1, area2 in combinations(areas, 2):
        if area1.isdisjoint(area2):
            continue

        result.update(area1)
        result.update(area2)

    return len(result)


assert solution("lx,ly,ux,uy\n0,0,3,3\n2,2,4,5\n6,3,8,7") == 14

print("Solution", solution(get_file_content("input11.csv")))
