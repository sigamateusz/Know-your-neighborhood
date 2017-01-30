from common import Common
from voivodeship import Voivodeship

def main():
    file_name = 'malopolska.csv'
    Common.load_file(file_name)

    maloposkie = Voivodeship.create_voivodeship()
    print(maloposkie.name)

if __name__ == '__main__':
    main()
