from collections import defaultdict
from itertools import takewhile
from utils import get_file_content
from functools import reduce
from math import sqrt

WORDS_PER_LENGTH = defaultdict(list)
for word in get_file_content("validwords15.txt").splitlines():
    WORDS_PER_LENGTH[len(word)].append(word)


def calculate(word: str):
    result = []
    memory = {}
    for letter in word:
        value_for_letter = sum(1 for l in word if letter > l) + memory.get(letter, 0)
        memory[letter] = memory.get(letter, 0) + 1
        result.append(value_for_letter)

    return tuple(result)


assert calculate('GLASS') == (1, 2, 0, 3, 4)
assert calculate('LEVER') == (2, 0, 4, 1, 3)


for word in WORDS_PER_LENGTH[5]:
    print(word, calculate(word))



def factors(n):
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


def perm(a, k=0):
    if k == len(a):
        print(a)
    else:

        for i in range(k, len(a)):
            a[k], a[i] = a[i] ,a[k]

            if a[0] != ' ':
                perm(a, k+1)
            else:
                pass

            a[k], a[i] = a[i], a[k]


def solution(encrypted: str) -> str:
    encrypted = encrypted.lower()
    limit = len(encrypted)

    for factor in factors(limit):
        if factor in WORDS_PER_LENGTH:
            print(factor)
            a = encrypted[:: limit // factor]
            perm(list(a))


assert solution(" DV  NWECEE E ODEOAIEFACRSRLTE") == "glass"

print("Solution", solution(get_file_content("input35.txt")[:-1]))
