from utils import get_file_content


def solution(content: str) -> int:
    instructions = list(
        map(tuple, map(lambda line: map(int, line.split(" ")), content.splitlines()))
    )

    instructions_max = len(instructions)
    direction = 1
    floor = 0
    visited_floors = 1

    while 0 <= floor < instructions_max:
        direction = direction * -1 if instructions[floor][0] == 0 else direction
        floor += direction * instructions[floor][1]
        visited_floors += 1

    return visited_floors


assert solution("1 2\n0 3\n1 1\n0 1\n1 5") == 7

print("Solution", solution(get_file_content("input12.txt")))
