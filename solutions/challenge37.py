from typing import List, Tuple
from utils import get_file_content, parse_as_csv_content


WORDS = set(
    word for word in get_file_content("validwords15.txt").splitlines() if len(word) == 5
)


def transformation(source):
    for row in source:
        yield row[0], list(map(int, row[1].split(" ")))


def is_word_matching(word, template, cannot_be_letters: set):
    letters_to_check = []
    letters_needs_to_be = []
    for letter, tile in zip(word, template):
        if isinstance(tile, str):
            if letter != tile:
                return False
            else:
                continue

        if isinstance(tile, list):
            if letter in tile:
                return False

            letters_needs_to_be.extend(tile)

        letters_to_check.append(letter)

    if not set(letters_needs_to_be).issubset(letters_to_check):
        return False

    return cannot_be_letters.isdisjoint(letters_to_check)


def count_word_value(word):
    letter_a = ord("a")

    return sum(ord(character) - letter_a for character in word)


def find_the_words(source: List[Tuple[str, List[int]]]) -> str:
    possibilities = None

    for guess, score in transformation(parse_as_csv_content(source)):
        print(guess, score)

        if not possibilities:
            possibilities = WORDS.copy()
            template = [None] * 5
            cannot_be_letters = set()

        possibilities.remove(guess)

        for letter, value, index in zip(guess, score, range(5)):
            if value == 2:
                template[index] = letter
                for temp in template:
                    if isinstance(temp, list) and letter in temp:
                        temp.remove(letter)
                        break

            elif value == 1:
                if not isinstance(template[index], list):
                    template[index] = []

                template[index].append(letter)

            elif value == 0:
                cannot_be_letters.add(letter)

        possibilities = set(
            word for word in possibilities if is_word_matching(word, template, cannot_be_letters)
        )

        assert len(possibilities) > 0

        if len(possibilities) == 1:
            print(next(iter(possibilities)))
            yield next(iter(possibilities))
            possibilities = None


def solution(content):
    return sum(count_word_value(word) for word in find_the_words(content))


print("Solution", solution(get_file_content("input37.csv")))
