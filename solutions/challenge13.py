from utils import get_file_content


def floyds_cycle_detection_algorithm(value: str) -> int:
    for index, character in enumerate(value):
        if value.count(character, index + 1) == 0:
            continue

        the_next_char_position = value.index(value[index], index + 1)
        check = value[index:the_next_char_position]
        if check == value[the_next_char_position:the_next_char_position + the_next_char_position - index]:
            i = 0
            while True:
                if i * check not in value:
                    return i - 1

                i += 1

    return None


def solution(content: str):
    return sum(
        floyds_cycle_detection_algorithm(line)
        for line in content.splitlines()
    )

assert floyds_cycle_detection_algorithm("ABCABCABCABCABC") == 5
assert floyds_cycle_detection_algorithm("AAAAAAB") == 6
assert floyds_cycle_detection_algorithm("ABCDEAAAAAAACCAF") == 7

print('Solution', solution(get_file_content("input13.txt")))
