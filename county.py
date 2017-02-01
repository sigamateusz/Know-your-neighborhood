from classes import *
from common import Common


class County(City):
    def __init__(self, name, kind):
        super().__init__(name, kind)
        self.municipality = []
        self.town_with_district_rights = []
        self.rural_area = []
        self.rural_commune = []
        self.urban_rural_commune = []
        self.cities = []
        self.delegacy = []

    @classmethod
    def create_county(cls, row_number, kind):
        county = cls(Common.file_loaded[row_number][4], kind)
        county_number = Common.file_loaded[row_number][1]
        for row in Common.file_loaded[row_number+1:]:
            if row[1] != county_number:
                break
            if row[3] == '1':
                county.municipality.append(Municipality(row[4], 'gmina miejska'))

            elif row[3] == '2':
                county.rural_commune.append(RuralCommune(row[4], 'wiejska'))

            elif row[3] == '3':
                county.urban_rural_commune.append(UrbanRuralCommune(row[4], 'gmina miejsko - wiejska'))

            elif row[3] == '4':
                county.cities.append(City(row[4], 'miasto'))

            elif row[3] == '5':
                county.rural_area.append(RuralArea(row[4], 'obszar wiejski'))

            elif row[3] == '9':
                county.delegacy.append(Delegacy(row[4], 'delegatura'))

        return county

    # def get_name(self):
    #     return self.name

