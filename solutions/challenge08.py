from typing import Generator, Tuple
from utils import get_file_content


def get_data(content: str) -> Generator[Tuple[str, int, str, int], None, None]:
    lines = content.splitlines()

    for day_id, line in enumerate(lines[1:]):
        cells = line.split(",")
        yield day_id, int(cells[1]), int(cells[2])


own_milk = {}
own_cereal = 0


for day_id, milk, bought_cereal in get_data(get_file_content('input08.csv')):
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


print('Solution', sum(own_milk.values()) + own_cereal)
