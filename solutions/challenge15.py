from collections import defaultdict, deque
from utils import get_file_content

WORDS = defaultdict(list)

for word in get_file_content('validwords15.txt').splitlines():
    WORDS[len(word)].append(word)


def words_difference(first_word: str, second_word: str) -> int:
    return sum(0 if f == s else 1 for f, s in zip(first_word, second_word))


def is_words_single_characters_difference(first_word: str, second_word: str):
    return words_difference(first_word, second_word) == 1

def index_of_words_difference(first_word: str, second_word: str) -> int:
    for index, (f, s) in enumerate(zip(first_word, second_word)):
        if f != s:
            return index

    return -1


def find_the_shortest_path(start_word: str, end_word: str) -> int:
    word_size = len(start_word)
    was = set()
    possibilities = deque([(start_word, 0)])

    while possibilities:
        word, step = possibilities.popleft()
        if word not in was:
            was.add(word)

            if word == end_word:
                return step + 1

            for neighbor in WORDS[word_size]:
                if not neighbor in was and words_difference(word, neighbor) == 1:
                    possibilities.append((neighbor, step + 1))

    raise Exception('Not found')


def solution(content: str) -> int:
    result = 1

    for line in content.splitlines():
        start_word, end_word = line.split(',')
        result *= find_the_shortest_path(start_word, end_word)

    return result


assert is_words_single_characters_difference('fly', 'fly') == False
assert is_words_single_characters_difference('fly', 'fry') == True
assert is_words_single_characters_difference('fly', 'try') == False
assert is_words_single_characters_difference('fly', 'trx') == False

assert find_the_shortest_path('word', 'maze') == 5

assert solution('fly,try\ntry,fly\nword,maze') == 45

print('Solution', solution(get_file_content('input15.txt')))
