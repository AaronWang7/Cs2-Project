# The program to read and write the word count number
def read_file(file_name: str):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print('File not found.')
        return ''


def write_file(file_name: str, content: str) -> None:
    with open(file_name, 'w') as file:
        file.write(content)
