from typing import Iterable
from utils import get_file_content, get_file_raw_content
from string import ascii_uppercase


GLYPH_HEIGHT = 6


def split_letters(lines: Iterable[str]):
    args = [iter(lines)] * GLYPH_HEIGHT
    return zip(*args)


def map_glyph(lines: Iterable[str]) -> set:
    return set(
        (row_index, column_index)
        for row_index, line in enumerate(lines)
        for column_index, character in enumerate(line)
        if character == "#"
    )


def display(pixels: set) -> str:
    max_column = max(column for _, column in pixels) + 1

    return "\n".join(
        "".join("#" if (row, column) in pixels else "." for column in range(max_column))
        for row in range(GLYPH_HEIGHT)
    )


def make_ascii_text(glyphs: dict, text: str) -> set:
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
                pixels.update(
                    set((row, column + cursor) for row, column in glyphs[letter])
                )
                break

    return pixels


def count_negative_space(pixels: set) -> int:
    return GLYPH_HEIGHT * (max(column for _, column in pixels) + 1) - len(pixels)


def solution(text: str) -> int:
    glyphs = {
        letter: map_glyph(glyph)
        for letter, glyph in zip(
            ascii_uppercase,
            split_letters(get_file_raw_content("asciialphabet16.txt").splitlines()),
        )
    }

    return count_negative_space(make_ascii_text(glyphs, text))


assert solution("LTA") == 53

print("Solution", solution(get_file_content("input16.txt")))
