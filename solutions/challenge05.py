from utils import get_file_content


def rotate(dice: list[str], direction: str) -> list[str]:
    if direction in "UD":
        dice[0], dice[2] = dice[2], dice[0]
    elif direction in "LR":
        dice[0], dice[1] = dice[1], dice[0]

    return dice


def solution(instruction: str) -> int:
    # Front, Left, Top
    dice1 = [1, 2, 3]
    dice2 = [1, 3, 2]
    result = 0

    for index, direction in enumerate(instruction):
        dice1 = rotate(dice1, direction)
        dice2 = rotate(dice2, direction)

        if dice1[0] == dice2[0]:
            result += index

    return result


assert solution("LRDLU") == 5

print("Solution", solution(get_file_content("input05.txt")))
