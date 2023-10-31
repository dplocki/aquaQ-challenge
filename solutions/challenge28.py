from itertools import count
from typing import Dict, Tuple
from utils import get_file_raw_content


def find_starting_location(mirrors: Dict[Tuple[int, int], str], letter: str) -> Tuple[int, int]:
    for row in count(1):
        if (row, 0) in mirrors and mirrors[row, 0] == letter:
            return row, 0

    raise Exception(f'Letter {letter} not found')


def ray_tracing(mirrors: Dict[Tuple[int, int], str], point: Tuple[int, int]) -> str:
    direction = 0, 1

    while True:
        point = point[0] + direction[0], point[1] + direction[1]
        if point not in mirrors:
            continue

        characters = mirrors[point]
        if characters not in '/\\':
            return characters
        elif characters == '/':
            direction = -1 * direction[1], -1 * direction[0]
            mirrors[point] = '\\'
        elif characters == '\\':
            direction = direction[1], direction[0]
            mirrors[point] = '/'


def encrypt(mirrors: str, text_to_encrypt: str) -> str:
    mirrors_map = {
        (row_index, column_index): character
        for row_index, line in enumerate(mirrors.splitlines())
        for column_index, character in enumerate(line)
        if character != ' '}

    return ''.join(ray_tracing(mirrors_map, find_starting_location(mirrors_map, letter)) for letter in text_to_encrypt)


test_input = ''' ABCD
A\  /A
B /\ B
C/ \ C
D/ / D
 ABCD '''

assert encrypt(test_input, 'DAD') == 'CCC'

print('Solution', encrypt(get_file_raw_content('input28.txt'), 'FISSION_MAILED'))
