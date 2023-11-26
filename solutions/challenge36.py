from functools import reduce
from math import sqrt
from utils import get_file_content


def factors(n):
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


def parser(content: str):
    for group in content.split("\n\n"):
        grid_raw, input_raw = group.splitlines()
        yield list(map(int, grid_raw[2:].split())), list(
            map(lambda r: None if r == "*" else int(r), input_raw[2:].split(" "))
        )


def recalculate_restriction(grid_numbers, composite_numbers):
    minium_limit = 0
    limiter = None

    for item in composite_numbers:
        if item == None:
            if limiter == None:
                limiter = [minium_limit, None, 1]
            else:
                limiter[2] += 1
        else:
            minium_limit = item
            if limiter != None:
                limiter[1] = item
                yield limiter
                limiter = None

    if limiter != None:
        limiter[1] = max(grid_numbers) - 1
        yield limiter


def find_all_potential_pairs(grid_numbers, composite_numbers, restrictions):
    solution_pairs = set()
    for gn in grid_numbers:

        for cn in composite_numbers:
            if cn != None and gn % cn == 0:
                other = gn // cn
                if (other + cn) in grid_numbers:
                    if is_matching_restriction(restrictions, other):
                        solution_pairs.add(tuple(sorted((cn, other))))

        for factor in factors(gn):
            other = gn // factor
            if factor + other in grid_numbers:
                if is_matching_restriction(restrictions, factor) and is_matching_restriction(restrictions, other):
                    solution_pairs.add(tuple(sorted((factor, other))))

    return solution_pairs


def is_matching_restriction(restrictions, value):
    for restriction in restrictions:
        if restriction[0] <= value <= restriction[1]:
            return True

    return False


def find_pairs(grid_numbers, composite_numbers):
    restrictions = list(recalculate_restriction(grid_numbers, composite_numbers))
    solution_pairs = find_all_potential_pairs(grid_numbers, composite_numbers, restrictions)

    for _s in solution_pairs:
        print(_s[0], _s[1])
        #print('\t', s, s[0] + s[1], s[0] * s[1])

    return solution_pairs


def solution(content: str):
    result = 0
    for grid_numbers, check_numbers in parser(content):
        a = find_pairs(grid_numbers, check_numbers)
        assert len(a) == 8
        for pair in a:
            result += abs(pair[0] - pair[1])

    return result


print('Solution', solution(get_file_content("input36.txt")))
