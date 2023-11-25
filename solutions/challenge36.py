from utils import get_file_content


def parser(content: str):
    for group in content.split("\n\n"):
        grid_raw, input_raw = group.splitlines()
        yield list(map(int, grid_raw[2:].split())), list(
            map(lambda r: None if r == "*" else int(r), input_raw[2:].split(" "))
        )


def find_pairs(grid_numbers, composite_numbers):
    solution_pairs = set()

    for gn in grid_numbers:
        for cn in composite_numbers:
            if cn != None and gn % cn == 0:
                if (gn // cn + cn) in grid_numbers:
                    solution_pairs.add(tuple(sorted((cn, gn // cn))))

    return solution_pairs


def solution(content: str):
    result = 0
    for grid_numbers, check_numbers in parser(content):
        for pair in find_pairs(grid_numbers, check_numbers):
            result += abs(pair[0] - pair[1])

    return result


print('Solution', solution(get_file_content("input36.txt")))
