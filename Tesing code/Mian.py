# Main program to handle user’s input
#import functions from other pages
from file_handling import read_file, write_file
from time_handling import get_timestamp


def main():
    #let the user enter the file name
    file_name = input('Enter the file name, copy the relative path: ')
    content = read_file(file_name)
    word_count = len(content.split())
    timestamp = get_timestamp()
    result = f'Word count: {word_count}\nLast updated: {timestamp}\n{content}'
    write_file(file_name, result)
    print('File updated successfully.')

# Run the program
if __name__ == '__main__':
    main()
