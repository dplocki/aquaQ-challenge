from utils import get_file_content

TEXT_ROOM_MAP = """  ##
 ####
######
######
 ####
  ##
""".splitlines()


def text_room_map_converter(text_map: [str]) -> dict:
    result = set()

    for row_index, line in enumerate(text_map):
        for column_index, character in enumerate(line):
            if character == "#":
                result.add((row_index, column_index))

    return result


def calculate_new_position(position, instruction):
    if instruction == "U":
        return (position[0] - 1, position[1])

    if instruction == "D":
        return (position[0] + 1, position[1])

    if instruction == "L":
        return (position[0], position[1] - 1)

    if instruction == "R":
        return (position[0], position[1] + 1)

    raise Exception(f"Unknown instruction {instruction}")


def walk(room_map: set, instructions: str) -> int:
    position = (0, 2)

    for instruction in instructions:
        new_position = calculate_new_position(position, instruction)
        if new_position in room_map:
            position = new_position

        yield position


def solution(instructions):
    result = 0
    for column, row in walk(text_room_map_converter(TEXT_ROOM_MAP), instructions):
        result += column + row

    return result


assert solution("UDRR") == 14

print("Solution", solution(get_file_content("input03.txt")))
