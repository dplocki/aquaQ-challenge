from utils import get_file_content


def get_data(content: str):
    lines = content.splitlines()

    for line in lines[1:]:
        first_player, second_player, score =  line.split(',')
        first_player_points, second_player_points = map(int, score.split('-'))

        yield first_player, first_player_points, second_player, second_player_points


def calculate_rate(ra, rb):
    return 1 / (1 + 10 ** ((rb-ra)/400))


def update_rating(rate):
    return 20 * (1 - rate)


def run_make(file_name: str):
    score_table = {}

    for first_player, first_player_points, second_player, second_player_points in get_data(get_file_content(file_name)):

        ra = score_table.get(first_player, 1200)
        rb = score_table.get(second_player, 1200)

        if first_player_points > second_player_points:
            rate = calculate_rate(ra, rb)
            score_table[first_player] = ra + update_rating(rate)
            score_table[second_player] = rb - update_rating(rate)
        else:
            rate = calculate_rate(rb, ra)
            score_table[first_player] = ra - update_rating(rate)
            score_table[second_player] = rb + update_rating(rate)

    return score_table


def solution(file_name: str):
    score_table = run_make(file_name)

    scores = score_table.values()

    return int(max(scores)) - int(min(scores))


print('Solution', solution('input07.txt'))
