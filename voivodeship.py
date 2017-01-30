from common import Common
from county import County


class Voivodeship:
    def __init__(self, name):
        self.name = name
        self.counties = []

    @classmethod
    def create_voivodeship(cls):
        voivodeship = cls(Common.file_loaded[0][4])
        for row in Common.file_loaded[1:]:
            if (row[2], row[3]) == ('', ''):

                name = row[1]
                new_county = County.create_county(name)
                voivodeship.counties.append(new_county)

        return voivodeship
