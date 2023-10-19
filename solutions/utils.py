from typing import Generator, Tuple


def get_file_raw_content(file_name: str) -> str:
    with open(file_name) as file:
        return file.read()


def get_file_content(file_name: str) -> str:
    return get_file_raw_content(file_name).strip()


def parse_as_csv_content(content: str) -> Generator[Tuple, None, None]:
    for line in content.splitlines()[1:]:
        yield line.split(",")
