from typing import List, Tuple
from utils import get_file_content, parse_as_csv_content


WORDS = set()
WORDS_TILES = {}
for word in (word for word in get_file_content("validwords15.txt").splitlines() if len(word) == 5):
    WORDS.add(word)

    letters = []
    for letter in word:
        letters.append(letter * (sum(1 for r in letters if r == letter) + 1))

    WORDS_TILES[word] = set(letters)


def transformation(source):
    for row in source:
        yield row[0], list(map(int, row[1].split(" ")))


def count_word_value(word):
    letter_a = ord("a")

    return sum(ord(character) - letter_a for character in word)


def find_the_words(source: List[Tuple[str, List[int]]]) -> str:
    possibilities = None

    for guess, score in transformation(parse_as_csv_content(source)):
        if possibilities == None:
            possibilities = WORDS.copy()
            reject_letters_tiles = set()
            word_template = [set() for _ in range(5)]

        possibilities.remove(guess)
        required_letters = set()
        current_letters_tiles = []
        for value, letter, index in sorted(zip(score, guess, range(5)), reverse=True):
            letter_title = letter * (sum(1 for l in current_letters_tiles if l == letter) + 1)

            current_letters_tiles.append(letter)
            if value == 2:
                word_template[index] = letter
                required_letters.add(letter_title)
            elif value == 1:
                word_template[index].add(letter)
                required_letters.add(letter_title)
            elif value == 0:
                reject_letters_tiles.add(letter_title)
                if len(letter_title) > 1:
                    word_template[index].add(letter)

        new_possibilities = set()
        for possibility in possibilities:
            if not (required_letters <= WORDS_TILES[possibility]):
                continue

            if not (reject_letters_tiles.isdisjoint(WORDS_TILES[possibility])):
                continue

            if (isinstance(word_template[0], set) and possibility[0] in word_template[0]) \
                or (isinstance(word_template[1], set) and possibility[1] in word_template[1]) \
                or (isinstance(word_template[2], set) and possibility[2] in word_template[2]) \
                or (isinstance(word_template[3], set) and possibility[3] in word_template[3]) \
                or (isinstance(word_template[4], set) and possibility[4] in word_template[4]):
                continue

            if (isinstance(word_template[0], str) and word_template[0] != possibility[0]) \
                or (isinstance(word_template[1], str) and word_template[1] != possibility[1]) \
                or (isinstance(word_template[2], str) and word_template[2] != possibility[2]) \
                or (isinstance(word_template[3], str) and word_template[3] != possibility[3]) \
                or (isinstance(word_template[4], str) and word_template[4] != possibility[4]):
                continue

            new_possibilities.add(possibility)

        possibilities = new_possibilities

        if len(possibilities) == 1:
            yield next(iter(possibilities))
            possibilities = None


def solution(content):
    return sum(count_word_value(word) for word in find_the_words(content))


assert count_word_value('words') + count_word_value('mince') == 113

print("Solution", solution(get_file_content("input37.csv")))