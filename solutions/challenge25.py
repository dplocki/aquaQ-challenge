from itertools import pairwise
from typing import List
from utils import get_file_content

MORSE_CODE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
}


def parse_time(value: str):
    raw_time, raw_millisecond = value.split(".")
    tokens_time = list(map(int, raw_time.split(":")))

    return ((tokens_time[0] * 60 + tokens_time[1]) * 60 + tokens_time[2]) * 1000 + int(
        raw_millisecond
    )


def transform_click_timestamps_to_delays(content: List[str]):
    for _to, _from in pairwise(map(parse_time, content.splitlines())):
        yield (_from - _to) // 717


def transform_to_letters(source):
    result = ""

    for index, units in enumerate(source):
        if index % 2 == 1:
            if units == 1:
                pass

            elif units == 3:
                yield MORSE_CODE[result]
                result = ""

            if units == 7:
                yield MORSE_CODE[result]
                result = ""
                yield " "
        else:
            if units == 1:
                result += "."

            elif units == 3:
                result += "-"

    yield MORSE_CODE[result]


for message in get_file_content("input25.txt").split("\n\n"):
    for letter in transform_to_letters(transform_click_timestamps_to_delays(message)):
        print(letter, end="")

    print()
