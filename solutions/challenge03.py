from typing import Tuple
from utils import get_file_content

TEXT_ROOM_MAP = """  ##
 ####
######
######
 ####
  ##
""".splitlines()


def text_room_map_converter(text_map: [str]) -> dict:
    return set(
        (row_index, column_index)
        for row_index, line in enumerate(text_map)
        for column_index, character in enumerate(line)
        if character == "#"
    )


def calculate_new_position(position: Tuple[int, int], instruction) -> Tuple[int, int]:
    if instruction == "U":
        return position[0] - 1, position[1]

    if instruction == "D":
        return position[0] + 1, position[1]

    if instruction == "L":
        return position[0], position[1] - 1

    if instruction == "R":
        return position[0], position[1] + 1

    raise Exception(f"Unknown instruction {instruction}")


def find_start_position(room_map: set) -> Tuple[int, int]:
    row_index = column_index = len(room_map)

    for current_row_index, column_index in room_map:
        column_index = min(column_index, current_row_index)
        row_index = min(row_index, current_row_index)

    return row_index, column_index


def walk(room_map: set, position: Tuple[int, int], instructions: str) -> int:
    for instruction in instructions:
        new_position = calculate_new_position(position, instruction)
        if new_position in room_map:
            position = new_position

        yield position


def solution(instructions: str) -> int:
    room_map = text_room_map_converter(TEXT_ROOM_MAP)

    return sum(
        column + row
        for column, row in walk(room_map, find_start_position(room_map), instructions)
    )


assert solution("UDRR") == 14

print("Solution", solution(get_file_content("input03.txt")))
