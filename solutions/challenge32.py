from utils import get_file_content

OPEN_BRACES = '([{'
CLOSE_BRACES = ')]}'


def is_braces_balanced(line: str) -> bool:
    stack = []

    for character in line:
        if character in OPEN_BRACES:
            stack.append(character)
        elif character in CLOSE_BRACES:
            if not stack:
                return False

            previous_brace = stack.pop()
            if CLOSE_BRACES[OPEN_BRACES.index(previous_brace)] != character:
                return False

    return len(stack) == 0


def solution(content: str) -> int:
    return sum(1 for line in content.splitlines() if is_braces_balanced(line))


assert is_braces_balanced("()") == True
assert is_braces_balanced("([]{})") == True
assert is_braces_balanced("(a[b[]]c){}") == True
assert is_braces_balanced(")()") == False
assert is_braces_balanced("([a)]") == False
assert is_braces_balanced("]{}[") == False
assert is_braces_balanced("((a)){]") == False


print("Solution", solution(get_file_content("input32.txt")))
