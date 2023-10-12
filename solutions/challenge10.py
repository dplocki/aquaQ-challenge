from utils import get_file_content


def parse_as_csv_content(content: str):
    for line in content.splitlines()[1:]:
        yield line.split(',')


def parse_wrapper(source):
    for user_a, user_b, cost in source:
        yield user_a.strip(), user_b.strip(), int(cost)


def solution(content: str, _from: str, _to: str) -> int:
    graph = {}
    users = set()

    for user_a, user_b, cost in parse_wrapper(parse_as_csv_content(content)):
        graph[user_a, user_b] = cost
        graph[user_b, user_a] = cost
        users.add(user_a)
        users.add(user_b)

    cost_so_far = {_from: 0}
    possibilities = [(_from, 0)]

    while possibilities:
        current, current_cost = possibilities.pop()

        for user in users:
            if (user, current) in graph:
                if cost_so_far.get(user, 9999999999999) > graph[user, current] + current_cost:
                    cost_so_far[user] = graph[user, current] + current_cost
                    possibilities.append((user, graph[user, current] + current_cost))

    return cost_so_far[_to]


assert solution('''s,d,c
A, B, 8
B, C, 50
B, D, 5
D, E, 10
E, C, 6''', 'A', 'C') == 29


print('Solution', solution(get_file_content('input10.csv'), 'Tupac'.upper(), 'Diddy'.upper()))
