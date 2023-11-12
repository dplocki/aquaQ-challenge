from typing import Generator, Iterable, Tuple


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
