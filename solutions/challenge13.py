from utils import get_file_content


def floyds_cycle_detection_algorithm(value: str) -> int:
    array = []

    for index, character in enumerate(value):
        the_next_char_position = value.find(character, index + 1)
        if the_next_char_position > 0:
            check = value[index:the_next_char_position]
            if check == value[the_next_char_position:the_next_char_position + the_next_char_position - index]:
                array.append(len(check))
                continue

        array.append(0)

    index = array.index(max(array))

    result = 1
    chuck = value[index:index + array[index]]

    while True:
        if result * chuck in value:
            result += 1
            continue

        return result - 1


def solution(content: str):
    return sum(
        floyds_cycle_detection_algorithm(line)
        for line in content.splitlines()
    )



assert floyds_cycle_detection_algorithm("BCDEAAHAHAHAHAHXC") == 5
assert floyds_cycle_detection_algorithm("ABCABCABCABCABC") == 5
assert floyds_cycle_detection_algorithm("AAAAAAB") == 6
assert floyds_cycle_detection_algorithm("ABCDEAAAAAAACCAF") == 7


print('Solution', solution(get_file_content("input13.txt")))
