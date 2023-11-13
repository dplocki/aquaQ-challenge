from typing import List, Tuple
from utils import get_file_content, parse_as_csv_content
from string import ascii_lowercase


WORDS = set(word
    for word in get_file_content("validwords15.txt").splitlines()
    if len(word) == 5)


def transformation(source):
    for row in source:
        yield row[0], list(map(int, row[1].split(' ')))


def is_word_matching(word, allowed_letters):
    return all(letter in allowed_letters
        for letter, allowed_letters in zip(word, allowed_letters))


def count_word_value(word):
    letter_a = ord("a")

    return sum(ord(character) - letter_a for character in word)


def split_guess_per_word(source):
    batch = []
    previous = 0

    for word, record in transformation(parse_as_csv_content(source)):
        actual = sum(record)
        if actual >= previous:
            batch.append((word, record))
            previous = actual
        else:
            yield batch
            batch = [(word, record)]
            previous = actual

    yield batch


def find_the_word(batch: List[Tuple[str, List[int]]]) -> str:
    possibilities = WORDS.difference(word for word, _ in batch)
    allowed_letters = [set(ascii_lowercase) for _ in range(5)]
    must_be_letters = set()

    for guess, score in batch:
        for letter, value, index in zip(guess, score, range(5)):
            if value == 2:
                allowed_letters[index] = set([letter])

        for letter, value, index in zip(guess, score, range(5)):
            if value == 0:
                for allowed_letter in allowed_letters:
                    if len(allowed_letter) > 1:
                        allowed_letter.discard(letter)

            elif value == 1:
                allowed_letters[index].remove(letter)
                must_be_letters.add(letter)

    possibilities = set(word
        for word in possibilities
        if is_word_matching(word, allowed_letters) and must_be_letters.issubset(word))

    assert len(possibilities) == 1

    return next(iter(possibilities))


def solution(content):
    result = 0
    for batch in split_guess_per_word(content):
        print(batch)
        result += count_word_value(find_the_word(batch))

    return result

    # return sum(
    #     count_word_value(find_the_word(batch))


solution(get_file_content('input37.csv'))
