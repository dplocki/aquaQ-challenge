from typing import Generator, Iterable, Tuple
from utils import get_file_content


def split_into_groups(source: Iterable, group_size: int) -> Generator[Tuple, None, None]:
    temporary = []
    for item in source:
        temporary.append(item)

        if len(temporary) == group_size:
            yield tuple(temporary)
            temporary = []


def neighbors(grid_size: int, point: Tuple[int, int]) -> Generator[Tuple, None, None]:
    row, column = point

    if row < grid_size - 1:
        yield row + 1, column

    if row > 0:
        yield row - 1, column

    if column < grid_size - 1:
        yield row, column + 1

    if column > 0:
        yield row, column - 1


def check_point(grid_size: int, state: set, point: Tuple) -> bool:
    return len(set(neighbors(grid_size, point)).intersection(state)) % 2 != 0


def points_to_check(grid_size, state: set) -> set:
    result = set()
    for point in state:
        result.update(neighbors(grid_size, point))

    return result


def run_simulation(line: str) -> int:
    tokens = map(int, line.split())
    maximum_steps = next(tokens)
    grid_size = next(tokens)
    state = set(split_into_groups(tokens, 2))

    for _ in range(maximum_steps):
        new_state = set()
        for point in points_to_check(grid_size, state):
            if check_point(grid_size, state, point):
                new_state.add(point)

        state = new_state

    return len(state)


def solution(content: str):
    return sum(run_simulation(line) for line in content.splitlines())


assert solution('350 6 2 2 2 3') == 8

print('Solution', solution(get_file_content('input19.txt')))
