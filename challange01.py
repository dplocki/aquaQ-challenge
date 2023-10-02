KEY_PAD = {
    1: None,
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
    0: ' '
}


def read_letter(KEY_PAD, key, times) -> str:
    letters = KEY_PAD[key]

    return letters[(times - 1) % len(letters)]


def x():
    with open('input01.txt', 'r') as file:
        content = file.readlines()

        for line in content:
            key, times = map(int, line.strip().split())


            yield read_letter(KEY_PAD, key, times)


assert read_letter(KEY_PAD, 7, 3) == 'r'

print(''.join(list(x())))