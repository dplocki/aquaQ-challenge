from collections import defaultdict, deque
from utils import get_file_content


def get_template_for_word(word: str):
    yield from (word[:i] + '_' + word[i + 1:] for i in range(len(word)))


WORDS = defaultdict(list)

for word in get_file_content('validwords15.txt').splitlines():
    for template in get_template_for_word(word):
        WORDS[template].append(word)


def find_the_shortest_path(start_word: str, end_word: str) -> int:
    was = set()
    possibilities = deque([(start_word, 0)])

    while possibilities:
        word, step = possibilities.popleft()
        if word not in was:
            was.add(word)

            if word == end_word:
                return step + 1

            for template in get_template_for_word(word):
                for neighbor in WORDS[template]:
                    if not neighbor in was:
                        possibilities.append((neighbor, step + 1))

    raise Exception('Not found')


def solution(content: str) -> int:
    result = 1

    for line in content.splitlines():
        start_word, end_word = line.split(',')
        result *= find_the_shortest_path(start_word, end_word)

    return result


assert find_the_shortest_path('word', 'maze') == 5

assert solution('fly,try\ntry,fly\nword,maze') == 45

print('Solution', solution(get_file_content('input15.txt')))
