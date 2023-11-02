from utils import get_file_content


def turn(deck, position: int):

    if (position - 1) in deck:
        deck[position - 1] = not deck[position - 1]

    if (position + 1) in deck:
        deck[position + 1] = not deck[position + 1]

    del deck[position]

    cards = len(deck)
    if len(deck) == 0:
        return True

    if sum(1 for i in deck.keys() if not i) == cards:
        return False

    for index in (index for index, card in deck.items() if card):
        if turn(deck.copy(), index):
            return True

    return False


def count_winning_positions(raw_deck: str) -> int:
    deck = {index: (card == "1") for index, card in enumerate(raw_deck)}

    to_check = [index for index, card in deck.items() if card]

    return sum(1 for start in to_check if turn(deck.copy(), start))


def solution(content: str) -> int:
    return sum(count_winning_positions(line) for line in content.splitlines())


assert count_winning_positions("11010") == 2
assert count_winning_positions("110") == 0
assert count_winning_positions("00101011010") == 3

print("Solution", solution(get_file_content("input30.txt")))
