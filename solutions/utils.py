from functools import reduce
from typing import Generator, Iterable, Set, Tuple


def factors(n: int) -> Set[int]:
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


def get_file_raw_content(file_name: str) -> str:
    with open(file_name) as file:
        return file.read()


def get_file_content(file_name: str) -> str:
    return get_file_raw_content(file_name).strip()


def parse_as_csv_content(
    content: str, skip_headers: bool = True
) -> Generator[Tuple, None, None]:
    source = iter(content.splitlines())
    if skip_headers:
        next(source)

    for line in source:
        yield line.split(",")


def split_into_groups(
    source: Iterable, group_size: int
) -> Generator[Tuple, None, None]:
    temporary = []
    for item in source:
        temporary.append(item)

        if len(temporary) == group_size:
            yield tuple(temporary)
            temporary = []
