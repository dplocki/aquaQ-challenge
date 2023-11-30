from collections import defaultdict
from typing import Dict
from utils import get_file_content
from functools import reduce
from math import sqrt


def build_words_per_length(file_name: str) -> Dict[int, str]:
    result = defaultdict(list)
    for word in get_file_content(file_name).splitlines():
        result[len(word)].append(word)

    return result


def factors(n):
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


def calculate(word: str):
    result = []
    memory = {}
    for letter in word:
        value_for_letter = sum(1 for l in word if letter > l) + memory.get(letter, 0)
        memory[letter] = memory.get(letter, 0) + 1
        result.append(value_for_letter)

    return tuple(result)


def find_solo_combination(word_length: int):
    counter = {}
    result = {}

    for word in WORDS_PER_LENGTH[word_length]:
        code = calculate(word)
        counter[code] = counter.get(code, 0) + 1
        result[code] = word

    for code, count in counter.items():
        if count != 1:
            del result[code]

    return result


def solution(words_per_length: Dict[int, str], encrypted: str) -> str:
    limit = len(encrypted)

    for word_length in factors(limit):
        if word_length in words_per_length:
            words = find_solo_combination(word_length)

            if len(words) == 0:
                continue

            print(word_length)
            print(words)


assert calculate("GLASS") == (1, 2, 0, 3, 4)
assert calculate("LEVER") == (2, 0, 4, 1, 3)

WORDS_PER_LENGTH = build_words_per_length("validwords15.txt")
print("Solution", solution(WORDS_PER_LENGTH, get_file_content("input35.txt")[:-1]))
