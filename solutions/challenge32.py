from utils import get_file_content


def is_braces_balanced(line: str) -> bool:
    stack = []

    for character in line:
        if character in '([{':
            stack.append(character)
        elif character in ')]}':
            if not stack:
                return False

            previous_brace = stack.pop()

            if previous_brace == '(' and character != ')':
                return False

            if previous_brace == '[' and character != ']':
                return False

            if previous_brace == '{' and character != '}':
                return False

    return len(stack) == 0


def solution(content: str) -> int:
    return sum(1
            for line in content.splitlines()
            if is_braces_balanced(line)
        )


assert is_braces_balanced('()') == True
assert is_braces_balanced('([]{})') == True
assert is_braces_balanced('(a[b[]]c){}') == True
assert is_braces_balanced(')()') == False
assert is_braces_balanced('([a)]') == False
assert is_braces_balanced(']{}[') == False
assert is_braces_balanced('((a)){]') == False


print('Solution', solution(get_file_content('input32.txt')))
