from typing import List, Tuple
from utils import get_file_content, parse_as_csv_content
from string import ascii_lowercase


WORDS = set(
    word for word in get_file_content("validwords15.txt").splitlines() if len(word) == 5
)


def transformation(source):
    for row in source:
        yield row[0], list(map(int, row[1].split(" ")))


def is_word_matching(word, allowed_letters, must_be_letters: set):
    letter_to_check = []
    for letter, single_allowed_letters in zip(word, allowed_letters):
        if letter not in single_allowed_letters:
            return False

        if len(single_allowed_letters) > 1:
            letter_to_check.append(letter)

    return must_be_letters.issubset(letter_to_check)


def count_word_value(word):
    letter_a = ord("a")

    return sum(ord(character) - letter_a for character in word)


def find_the_words(source: List[Tuple[str, List[int]]]) -> str:
    possibilities = None

    for guess, score in transformation(parse_as_csv_content(source)):
        print("\t", guess, score)
        if possibilities == None:
            possibilities = WORDS.copy()
            allowed_letters = [set(ascii_lowercase) for _ in range(5)]
            must_be_letters = set()

        possibilities.remove(guess)
        for letter, value, index in zip(guess, score, range(5)):
            if value == 2:
                if len(allowed_letters[index]) > 1 and letter in must_be_letters:
                    must_be_letters.remove(letter)

                allowed_letters[index] = set([letter])

        for letter, value, index in zip(guess, score, range(5)):
            if value == 0:
                if letter in must_be_letters:
                    continue

                for allowed_letter in allowed_letters:
                    if len(allowed_letter) > 1:
                        allowed_letter.discard(letter)

            elif value == 1:
                allowed_letters[index].remove(letter)
                must_be_letters.add(letter)

        possibilities = set(
            word for word in possibilities if is_word_matching(word, allowed_letters, must_be_letters)
        )

        if len(possibilities) == 1:
            print(next(iter(possibilities)))
            yield next(iter(possibilities))
            possibilities = None


def solution(content):
    return sum(count_word_value(word) for word in find_the_words(content))


print("Solution", solution(get_file_content("input37.csv")))