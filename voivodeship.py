from common import Common
from county import County
from town_with_district_rights import TownWithDistrictRights


class Voivodeship:
    def __init__(self, name):
        self.name = name
        self.counties = []
        self.towns_with_district_rights = []

    @classmethod
    def create_voivodeship(cls):
        voivodeship = cls(Common.file_loaded[0][4])
        row_number = 1
        for row in Common.file_loaded[1:]:
            if (row[2], row[3]) == ('', ''):
                if row[4][0].isupper():
                    new_town = TownWithDistrictRights.create_county(row_number)
                    voivodeship.towns_with_district_rights.append(new_town)
                else:
                    new_county = County.create_county(row_number)
                    voivodeship.counties.append(new_county)
            row_number += 1

        return voivodeship

    def get_name(self):
        return self.name
