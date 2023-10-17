from collections import defaultdict, deque
from heapq import heappop, heappush
from utils import get_file_content

WORDS = defaultdict(list)

for word in get_file_content('validwords15.txt').splitlines():
    WORDS[len(word)].append(word)


def words_difference(first_word: str, second_word: str) -> int:
    return sum(0 if f == s else 1 for f, s in zip(first_word, second_word))


def is_words_single_characters_difference(first_word: str, second_word: str):
    return words_difference(first_word, second_word) == 1


def find_the_shortest_path(start_word: str, end_word: str) -> int:
    word_size = len(start_word)

    possibilities = [ ]
    heappush(possibilities, (words_difference(start_word, end_word), [start_word]))

    while possibilities:
        _, path = heappop(possibilities)
        last_word = path[-1]

        if last_word == end_word:
            return len(path)

        for word in WORDS[word_size]:
            if is_words_single_characters_difference(last_word, word) and word not in path:
                heappush(possibilities, (words_difference(word, end_word), path + [word]))

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
