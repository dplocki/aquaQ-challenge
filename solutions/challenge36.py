from functools import reduce
from typing import Generator, List, Set, Tuple
from utils import factors, get_file_content, split_into_groups


def parser(content: str) -> Generator[Tuple[List[int], List[int]], None, None]:
    for group in content.split("\n\n"):
        grid_raw, input_raw = group.splitlines()
        yield list(map(int, grid_raw[2:].split())), list(
            map(lambda r: None if r == "*" else int(r), input_raw[2:].split(" "))
        )


def recalculate_restriction(
    grid_numbers: List[int], composite_numbers: List[int]
) -> Generator[Tuple[int, int], None, None]:
    minium_limit = 0
    limiter = None

    for item in composite_numbers:
        if item == None:
            if limiter == None:
                limiter = [minium_limit, None]
        else:
            minium_limit = item
            if limiter != None:
                limiter[1] = item
                yield limiter
                limiter = None

    if limiter != None:
        limiter[1] = max(grid_numbers) - 1
        yield limiter


def is_matching_restriction(restrictions: Tuple[int, int], value: int) -> bool:
    for restriction in restrictions:
        if restriction[0] <= value <= restriction[1]:
            return True

    return False


def find_all_potential_pairs(
    grid_numbers: List[int],
    composite_numbers: List[int],
    restrictions: List[Tuple[int, int]],
) -> Set[Tuple[int, int]]:
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
                if is_matching_restriction(
                    restrictions, factor
                ) and is_matching_restriction(restrictions, other):
                    solution_pairs.add(tuple(sorted((factor, other))))

    return solution_pairs


def find_matching_pairs(
    grid_numbers: List[int],
    input_numbers: List[int],
    potential_pairs: Set[Tuple[int, int]],
    solution: List[int],
) -> List[int]:
    if len(solution) == 16:
        for a, b in zip(sorted(solution), input_numbers):
            if b == None:
                continue

            if a != b:
                return None

        return solution

    grid_number = grid_numbers[0]
    for left, right in potential_pairs:
        if (left + right != grid_number) and (left * right != grid_number):
            continue

        if (left + right not in grid_numbers) or (left * right not in grid_numbers):
            continue

        grid_numbers_copy = grid_numbers.copy()
        solution_copy = solution.copy()

        grid_numbers_copy.remove(left + right)
        grid_numbers_copy.remove(left * right)

        solution_copy.append(left)
        solution_copy.append(right)

        result = find_matching_pairs(
            grid_numbers_copy, input_numbers, potential_pairs, solution_copy
        )
        if result != None:
            return result

    return None


def find_pairs(
    grid_numbers: List[int], input_numbers: List[int]
) -> List[Tuple[int, int]]:
    restrictions = list(recalculate_restriction(grid_numbers, input_numbers))
    potential_pairs = find_all_potential_pairs(
        grid_numbers, input_numbers, restrictions
    )
    matching_input_numbers = find_matching_pairs(
        grid_numbers, input_numbers, potential_pairs, []
    )

    return list(split_into_groups(matching_input_numbers, 2))


def solution(content: str) -> int:
    result = 0
    for grid_numbers, input_numbers in parser(content):
        a = find_pairs(grid_numbers, input_numbers)
        for pair in a:
            result += abs(pair[0] - pair[1])

    return result


print("Solution", solution(get_file_content("input36.txt")))
