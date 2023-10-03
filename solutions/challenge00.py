from typing import Iterator, Tuple


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


def load_file_content(file_name: str) -> Iterator[str]:
    with open(file_name, "r") as file:
        yield from file.readlines()


def read_letter(KEY_PAD, key, times) -> str:
    letters = KEY_PAD[key]

    return letters[(times - 1) % len(letters)]


def parse_input(file_name: str) -> Iterator[Tuple[int, int]]:
    for line in load_file_content(file_name):
        yield map(int, line.strip().split())


def decode_message(instructions: Iterator[Tuple[int, int]]) -> Iterator[str]:
    for key, times in instructions:
        yield read_letter(KEY_PAD, key, times)


assert read_letter(KEY_PAD, 7, 3) == "r"

print("Solution:", "".join(decode_message(parse_input("input00.txt"))))
