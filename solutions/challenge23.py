from typing import Dict, Tuple
from utils import get_file_content, split_into_groups
from string import ascii_lowercase

KEY_TABLE_SIZE = 5

def prepear_decoding_table(keyword: str) -> Dict[Tuple[int, int], str]:

    a = keyword.lower().replace(' ', '')
    used_letters = set('j')
    result = {}

    index = 0
    for letter in a + ascii_lowercase:
        if letter in used_letters:
            continue

        used_letters.add(letter)
        result[index // KEY_TABLE_SIZE, index % KEY_TABLE_SIZE] = letter
        index += 1
        if index == 25:
            break

    return result


def reverse_dictionary(origin: Dict) -> Dict:
    return { value:key for key, value in origin.items() }


def playfair_cipher_decryption(key_table: Dict[Tuple[int, int], str], encrypted_message: str) -> str:
    reverse_key_table = reverse_dictionary(key_table)
    result = ''

    for first, second in split_into_groups(encrypted_message, 2):
        first_position = reverse_key_table[first]
        second_position = reverse_key_table[second]

        if first_position[0] == second_position[0]:
            result += key_table[first_position[0], (first_position[1] - 1) % KEY_TABLE_SIZE]
            result += key_table[second_position[0], (second_position[1] - 1) % KEY_TABLE_SIZE]
            continue

        if first_position[1] == second_position[1]:
            result += key_table[(first_position[0] - 1) % KEY_TABLE_SIZE, first_position[1]]
            result += key_table[(second_position[0] - 1) % KEY_TABLE_SIZE, second_position[1]]
            continue

        result += key_table[first_position[0], second_position[1]]
        result += key_table[second_position[0], first_position[1]]

    return result


def solution(content: str) -> str:
    return playfair_cipher_decryption(prepear_decoding_table('power plant'), content)


print('Solution', solution(get_file_content('input23.txt')))
