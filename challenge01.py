def get_file_content(file_name: str) -> str:
    with open(file_name) as file:
        return file.read()


def conversion_process(value: str) -> str:

    def is_hex(character: str) -> bool:
        return '0' <= character <= '9' or 'a' <= character <= 'f'

    value_size = len(value)
    require_size = (value_size // 3 + 1) * 3
    extended_value = value.lower() + (require_size - value_size) * '0'
    characters = list(map(lambda character: character if is_hex(character) else '0', extended_value))
    characters_size = require_size // 3

    return ''.join(characters[:characters_size][:2] + characters[characters_size:characters_size * 2][:2] + characters[characters_size * 2:][:2])


assert conversion_process('kdb4life') == '0d40fe'

print('Solution', conversion_process(get_file_content('input01.txt')))
