from utils import get_file_content


def find_sum_of_correct_numbers(tablet: str) -> int:
    was_number = {}
    content = []

    for number in map(int, tablet.split()):
        if number in was_number:
            for incorrect_number in content[was_number[number] + 1 :]:
                del was_number[incorrect_number]

            content = content[: was_number[number]]
        else:
            was_number[number] = len(content)

        content.append(number)

    return sum(content)


assert find_sum_of_correct_numbers("1 4 3 2 4 7 2 6 3 6") == 20

print("Solution", find_sum_of_correct_numbers(get_file_content("input03.txt")))
