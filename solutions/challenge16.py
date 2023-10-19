from utils import get_file_content, get_file_raw_content
from string import ascii_uppercase


GLYPH_HEIGHT = 6


def split_letters(lines):
    args = [iter(lines)] * GLYPH_HEIGHT
    return zip(*args)


def map_glyph(lines: [str]) -> set:
    glyph = set()

    for row_index, line in enumerate(lines):
        for column_index, character in enumerate(line):
            if character == '#':
                glyph.add((row_index, column_index))

    return glyph


def display(pixels: set):
    max_column = max(column for _, column in pixels) + 1
    result = ''
    for row in range(6):
        for column in range(max_column):
            if (row, column) in pixels:
                result += '#'
            else:
                result += '.'

        result += '\n'

    return result

glyphs = {
    letter: map_glyph(glyph)
    for letter, glyph in zip(ascii_uppercase, split_letters(get_file_raw_content('asciialphabet16.txt').splitlines()))
}


def make_ascii_text(text: str):
    pixels = set()

    cursor = -1
    for letter in text:
        while True:
            cursor += 1
            potential_letter = set()
            for row, column in glyphs[letter]:
                potential_letter.add((row, column + cursor - 1))
                potential_letter.add((row, column + cursor))

            if pixels.isdisjoint(potential_letter):
                pixels.update(set((row, column + cursor) for row, column in glyphs[letter]))
                break

    return pixels


def count_negative_space(pixels: set) -> int:
    return GLYPH_HEIGHT * (max(column for _, column in pixels) + 1) - len(pixels)


def solution(text: str) -> int:
    return count_negative_space(make_ascii_text(text))


assert solution('LTA') == 53

print('Solution', solution(get_file_content('input16.txt')))
