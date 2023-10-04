def get_file_content(file_name: str) -> str:
    with open(file_name) as file:
        return file.read().strip()


def solution(tablet: str) -> int:
    was = {}
    content = []

    for number in map(int, tablet.split()):
        if number in was:
            for n in content[was[number] + 1:]:
                del was[n]

            content = content[: was[number]]
        else:
            was[number] = len(content)

        content.append(number)

    return sum(content)


assert solution("1 4 3 2 4 7 2 6 3 6") == 20

print("Solution", solution(get_file_content("input03.txt")))
