from collections import defaultdict
from typing import Dict, Set
from utils import get_file_content
from functools import reduce
from math import sqrt


def build_words_per_length(file_name: str) -> Dict[int, str]:
    result = defaultdict(list)
    for word in get_file_content(file_name).splitlines():
        result[len(word)].append(word)

    return result


def factors(n: int) -> Set[int]:
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


def find_solo_combination(words_per_length: Dict[int, str], word_length: int):
    counter = {}
    result = {}

    for word in words_per_length[word_length]:
        code = calculate(word)
        counter[code] = counter.get(code, 0) + 1
        result[code] = word

    for code, count in counter.items():
        if count != 1:
            del result[code]

    return result


def decode(encoded_text: str, code):
    limit = len(encoded_text)
    code_length = len(code)
    result = []

    for i in range(limit // code_length):
        line = encoded_text[i :: limit // code_length]
        for c in code:
            result.append(line[c])

    return "".join(result)


def solution(words_per_length: Dict[int, str], encrypted_text: str) -> str:
    limit = len(encrypted_text)

    for word_length in factors(limit):
        first_line = encrypted_text[:: limit // word_length]

        if word_length in words_per_length:
            words = find_solo_combination(words_per_length, word_length)

            for code, word in words.items():
                decoded_first_line = "".join(first_line[c] for c in code)

                if (
                    not decoded_first_line[0].isupper()
                    or "  " in decoded_first_line
                    or " '" in decoded_first_line
                ):
                    continue

                tokens = decoded_first_line.split(" ")
                first_decoded_word = tokens[0].lower()
                if (
                    first_decoded_word not in words_per_length[len(first_decoded_word)]
                    or len(tokens) > 2
                    and tokens[1].lower() not in words_per_length[len(tokens[1])]
                ):
                    continue

                decrypted_text = decode(encrypted_text, code)
                tokens = list(
                    filter(
                        lambda t: len(t) > 1,
                        decrypted_text[:30]
                        .lower()
                        .replace(",", "")
                        .replace(".", "")
                        .split(" "),
                    )
                )
                if all(token in words_per_length[len(token)] for token in tokens[:-1]):
                    yield word, decrypted_text


assert calculate("GLASS") == (1, 2, 0, 3, 4)
assert calculate("LEVER") == (2, 0, 4, 1, 3)
assert (
    decode(" DV  NWECEE E ODEOAIEFACRSRLTE", (1, 2, 0, 3, 4))
    == "WE ARE DISCOVERED FLEE AT ONCE"
)

WORDS_PER_LENGTH = build_words_per_length("validwords15.txt")

print("Code words + decoded text:")

for word, decoded_text in solution(
    WORDS_PER_LENGTH, get_file_content("input35.txt")[:-1]
):
    print("\t", word)
    print("----------------------")
    print("\t", decoded_text)
    print()
