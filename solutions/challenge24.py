from collections import Counter
from utils import get_file_content


class Node:
    def __init__(self, value: str, frequency: int, left=None, right=None) -> None:
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.value}:{self.frequency}"


def pass_by_tree(node, prefix):
    if node.left == None and node.right == None:
        yield node.value, prefix
        return

    yield from pass_by_tree(node.left, prefix + '0')
    yield from pass_by_tree(node.right, prefix + '1')


def build_decoding_dictionary(node):
    return {
        code: letter
        for letter, code in pass_by_tree(node, '')
    }


def build_tree(text: str):
    nodes = [Node(letter, frequency) for letter, frequency in Counter(text).items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda node: (node.frequency, node.value))

        nodes.append(
            Node(
                nodes[0].value + nodes[1].value,
                nodes[0].frequency + nodes[1].frequency,
                nodes[0],
                nodes[1],
            )
        )

        nodes = nodes[2:]

    return build_decoding_dictionary(nodes[0])


def decoding_message(decode_dictionary, encoded_text: str) -> str:
    result = []
    chunk = ''

    while encoded_text:
        chunk += encoded_text[0]
        encoded_text = encoded_text[1:]

        if chunk in decode_dictionary:
            result.append(decode_dictionary[chunk])
            chunk = ''

    return ''.join(result)


assert decoding_message(build_tree("A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"), '11101100011000') == 'CEDED'

lines = get_file_content('input24.txt').splitlines()
print('Solution:', decoding_message(build_tree(lines[0]), lines[1]))
