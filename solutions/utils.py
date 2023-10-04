def get_file_content(file_name: str) -> str:
    with open(file_name) as file:
        return file.read().strip()
