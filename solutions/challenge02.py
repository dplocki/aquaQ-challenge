from utils import get_file_content


def find_sum_of_correct_numbers(tablet: str) -> int:
    content = []

    for number in map(int, tablet.split()):
        if number in content:
            content = content[: content.index(number)]

        content.append(number)

    return sum(content)


assert find_sum_of_correct_numbers("1 4 3 2 4 7 2 6 3 6") == 20

print("Solution", find_sum_of_correct_numbers(get_file_content("input02.txt")))
