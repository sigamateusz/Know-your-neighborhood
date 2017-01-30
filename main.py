from common import Common
from menu import Menu


def main():
    file_name = 'malopolska.csv'
    Common.load_file(file_name)

    Menu.run()


if __name__ == '__main__':
    main()
