from common import Common


class TownWithDistrictRights:

    def __init__(self, name):
        self.name = name
        self.municipality = []
        self.town_with_district_rights = []
        self.rural_area = []
        self.rural_commune = []
        self.urban_rural_commune = []
        self.cities = []
        self.delegacy = []

    @classmethod
    def create_town(cls, row_number):
        town = cls(Common.file_loaded[row_number][4])
        town_number = Common.file_loaded[row_number][1]
        for row in Common.file_loaded[row_number + 1:]:
            if row[1] != town_number:
                break
            if row[3] == '1':
                town.municipality.append(row[4])

            elif row[3] == '2':
                town.rural_commune.append(row[4])

            elif row[3] == '3':
                town.urban_rural_commune.append(row[4])

            elif row[3] == '4':
                town.cities.append(row[4])

            elif row[3] == '5':
                town.rural_area.append(row[4])

            elif row[3] == '9':
                town.delegacy.append(row[4])

        return town

    def get_name(self):
        return self.name
