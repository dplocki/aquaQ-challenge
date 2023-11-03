from functools import lru_cache
from typing import Tuple
from utils import get_file_content


def get_possible_splits_of_deck(deck: str) -> Tuple[str, str]:
    index = deck.find('1', 0)
    while index > - 1:
        yield split_the_deck(deck, index)
        index = deck.find('1', index + 1)


@lru_cache
def can_win(deck: str) -> bool:
    if deck == None:
        return True

    if deck == '1':
        return True

    if deck.count('0') == len(deck):
        return False

    for part_generator in get_possible_splits_of_deck(deck):
        if not can_win(next(part_generator, None)):
            continue

        if not can_win(next(part_generator, None)):
            continue

        return True

    return False


def flip_card(card: str) -> str:
    return '1' if card == '0' else '0'


def split_the_deck(deck: str, index: int):
    if index > 0:
        yield deck[:index - 1] + flip_card(deck[index - 1])

    if index + 1 < len(deck):
        yield flip_card(deck[index + 1]) + deck[index + 2:]


def count_winning_positions(deck: str) -> int:
    return sum(1
        for part_generator in get_possible_splits_of_deck(deck)
        if all(map(can_win, part_generator)))


def solution(content: str) -> int:
    return sum(count_winning_positions(line) for line in content.splitlines())


assert count_winning_positions("11010") == 2
assert count_winning_positions("110") == 0
assert count_winning_positions("00101011010") == 3

print("Solution", solution(get_file_content("input30.txt")))
