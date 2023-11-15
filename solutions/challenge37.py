from typing import List, Tuple
from utils import get_file_content, parse_as_csv_content
from string import ascii_lowercase


WORDS = set(
    word for word in get_file_content("validwords15.txt").splitlines() if len(word) == 5
)


def transformation(source):
    for row in source:
        yield row[0], list(map(int, row[1].split(" ")))


def is_word_matching(word, word_template, required_letters):
    letter_to_check = []
    for letter, tile in zip(word, word_template):
        if isinstance(tile, str):
            if tile != letter:
                return False
            else:
                continue

        if isinstance(tile, set):
            if letter in tile:
                return False

        letter_to_check.append(letter)

    return all(letter in letter_to_check for letter in required_letters)


def count_word_value(word):
    letter_a = ord("a")

    return sum(ord(character) - letter_a for character in word)


def find_the_words(source: List[Tuple[str, List[int]]]) -> str:
    possibilities = None

    for guess, score in transformation(parse_as_csv_content(source)):
        print("\t", guess, score)
        if possibilities == None:
            possibilities = WORDS.copy()
            word_template = [set() for _ in range(5)]
            required_letters = []

        possibilities.remove(guess)
        for letter, value, index in zip(guess, score, range(5)):
            if value == 2:
                if letter in required_letters and isinstance(word_template[index], set):
                    required_letters.remove(letter)

                word_template[index] = letter

        for letter, value, index in zip(guess, score, range(5)):
            if value == 0:
                for tile in word_template:
                    if isinstance(tile, set) and letter not in required_letters:
                        tile.add(letter)

            elif value == 1:
                if letter not in required_letters:
                    required_letters.append(letter)
                word_template[index].add(letter)

        possibilities = set(
            word for word in possibilities if is_word_matching(word, word_template, required_letters)
        )

        if len(possibilities) == 1:
            print(next(iter(possibilities)))
            yield next(iter(possibilities))
            possibilities = None


def solution(content):
    return sum(count_word_value(word) for word in find_the_words(content))


print("Solution", solution(get_file_content("input37.csv")))