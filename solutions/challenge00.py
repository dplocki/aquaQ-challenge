from typing import Dict, Iterator, Tuple
from utils import get_file_content


KEY_PAD = {
    1: None,
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}


def read_letter(key_pad: Dict[int, str], key: int, times: int) -> str:
    letters = key_pad[key]

    return letters[(times - 1) % len(letters)]


def parse_input(content: str) -> Iterator[Tuple[int, int]]:
    for line in content.splitlines():
        yield map(int, line.strip().split())


def decode_message(
    key_pad: Dict[int, str], instructions: Iterator[Tuple[int, int]]
) -> Iterator[str]:
    for key, times in instructions:
        yield read_letter(key_pad, key, times)


def solution(content: str) -> str:
    return "".join(decode_message(KEY_PAD, parse_input(content)))


assert read_letter(KEY_PAD, 7, 3) == "r"

print("Solution:", solution(get_file_content("input00.txt")))
