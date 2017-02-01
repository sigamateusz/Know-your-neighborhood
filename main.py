from common import Common
from menu import Menu
import sys


def main():
    file_name = 'malopolska.csv'
    if len(sys.argv) > 1:  # checks whether the user has entered a file name
        file_name = sys.argv[1]

    Common.load_file(file_name)

    Menu.run()


if __name__ == '__main__':
    main()