from common import Common
from voivodeship import Voivodeship

def main():
    file_name = 'malopolska.csv'
    Common.load_file(file_name)

    maloposkie = Voivodeship.create_voivodeship()
    # print(maloposkie.counties[0].name)
    for county in maloposkie.counties:
        print('\n' + county + '\n')
        for delegatura in county.cities:
            print(delegatura)


if __name__ == '__main__':
    main()
