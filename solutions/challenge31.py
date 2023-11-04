from rubik.cube import Cube, FRONT

from functools import reduce
from operator import mul
from typing import Generator
from utils import get_file_content


def split_the_input(line: str) -> Generator[str, None, None]:
    index = 0
    limit = len(line)

    while index < limit:
        if index < limit - 1 and line[index + 1] == "'":
            yield line[index:index + 2]
            index += 2
        else:
            yield line[index]
            index += 1


def solution(instructions: str) -> int:
    cube = Cube("222222222333111444666333111444666333111444666555555555")

    for instruction in split_the_input(instructions):
        if instruction == 'F':
            cube.F()
        elif instruction == 'L':
            cube.L()
        elif instruction == 'R':
            cube.R()
        elif instruction == 'U':
            cube.U()
        elif instruction == 'D':
            cube.D()
        elif instruction == 'B':
            cube.B()
        elif instruction == 'F\'':
            cube.Fi()
        elif instruction == 'L\'':
            cube.Li()
        elif instruction == 'R\'':
            cube.Ri()
        elif instruction == 'U\'':
            cube.Ui()
        elif instruction == 'D\'':
            cube.Di()
        elif instruction == 'B\'':
            cube.Bi()

    return reduce(mul, (int(p.colors[2]) for p in sorted(cube._face(FRONT), key=lambda p: (-p.pos.y, p.pos.x))), 1)


assert solution("U'LBRU") == 960

print('Solution', solution(get_file_content('input31.txt')))