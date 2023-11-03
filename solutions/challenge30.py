from utils import get_file_content


def count_winning_positions(deck: str) -> int:
    ones = deck.count('1')
    if ones % 2 == 1:
        return ones // 2 + 1

    return 0


def solution(content: str) -> int:
    return sum(count_winning_positions(line) for line in content.splitlines())


assert count_winning_positions("11010") == 2
assert count_winning_positions("110") == 0
assert count_winning_positions("00101011010") == 3

print("Solution", solution(get_file_content("input30.txt")))
