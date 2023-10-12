from typing import Generator, Iterator, Tuple
from utils import get_file_content, parse_as_csv_content


def parse_wrapper(
    source: Iterator[Tuple],
) -> Generator[Tuple[int, int, int], None, None]:
    for day_id, cells in enumerate(source):
        yield day_id, int(cells[1]), int(cells[2])


def solution(content: str) -> int:
    own_milk = {}
    own_cereal = 0

    for day_id, milk, bought_cereal in parse_wrapper(parse_as_csv_content(content)):
        own_cereal += bought_cereal

        if own_cereal >= 100 and sum(own_milk.values()) >= 100:
            own_cereal -= 100

            oldest_milk_key = min(own_milk.keys())
            own_milk[oldest_milk_key] -= 100

            if own_milk[oldest_milk_key] == 0:
                del own_milk[oldest_milk_key]

        if day_id - 5 in own_milk:
            del own_milk[day_id - 5]

        own_milk[day_id] = milk

    return sum(own_milk.values()) + own_cereal


print("Solution", solution(get_file_content("input08.csv")))
