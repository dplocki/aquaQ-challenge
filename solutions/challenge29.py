from utils import get_file_content


def is_good_number(number):
    x = str(number)
    for a, b in zip(x, x[1:]):
        if a > b:
            return False

    return True


assert is_good_number(1)
assert is_good_number(45)
assert is_good_number(777)
assert is_good_number(1245)


def solution(maximum_number):
    return sum(1
        for i in range(int(maximum_number))
        if is_good_number(i)
    )


print('Solution', solution(get_file_content('input29.txt')))
