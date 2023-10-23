from typing import Dict
from utils import get_file_content

WINING_POINTS = 21


def build_card_values() -> Dict[str, int]:
    cards = {str(face): [face] for face in range(2, 11)}

    cards["J"] = [10]
    cards["Q"] = [10]
    cards["K"] = [10]
    cards["A"] = [1, 11]

    return cards


def solution(content: str) -> int:
    remove_losing_hands = lambda value: value < WINING_POINTS
    cards_values = build_card_values()
    cards = content.split()

    win_count = 0
    current_hand = [0]

    for card in cards:
        current_hand = [
            new_value + value
            for new_value in cards_values[card]
            for value in current_hand
        ]

        if WINING_POINTS in current_hand:
            win_count += 1
            current_hand = [0]
            continue

        current_hand = list(filter(remove_losing_hands, current_hand))

        if not current_hand:
            current_hand = [0]

    return win_count


assert solution("3 A K 9 A 7 4 9") == 1

print("Solution", solution(get_file_content("input20.txt")))
