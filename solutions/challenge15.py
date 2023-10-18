from collections import defaultdict, deque
from typing import Dict
from utils import get_file_content


def get_template_for_word(word: str):
    yield from (word[:i] + "_" + word[i + 1 :] for i in range(len(word)))


def build_wordbook(content: str) -> Dict[str, list]:
    result = defaultdict(list)

    for word in content.splitlines():
        for template in get_template_for_word(word):
            result[template].append(word)

    return result


def find_the_shortest_path(
    wordbook: Dict[str, list], start_word: str, end_word: str
) -> int:
    was = set()
    possibilities = deque([(start_word, 1)])

    while possibilities:
        word, step = possibilities.popleft()
        if word not in was:
            was.add(word)

            if word == end_word:
                return step

            for template in get_template_for_word(word):
                for neighbor in wordbook[template]:
                    if not neighbor in was:
                        possibilities.append((neighbor, step + 1))

    raise Exception("Not found")


def solution(wordbook: Dict[str, list], content: str) -> int:
    result = 1

    for line in content.splitlines():
        start_word, end_word = line.split(",")
        result *= find_the_shortest_path(wordbook, start_word, end_word)

    return result


wordbook = build_wordbook(get_file_content("validwords15.txt"))

assert find_the_shortest_path(wordbook, "word", "maze") == 5
assert solution(wordbook, "fly,try\ntry,fly\nword,maze") == 45

print("Solution", solution(wordbook, get_file_content("input15.txt")))
