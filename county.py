from classes import *
from common import Common


class County(Location):
    def __init__(self, name, kind='powiat'):
        super().__init__(name, kind)
        self.municipality = []
        self.town_with_district_rights = []
        self.rural_area = []
        self.rural_commune = []
        self.urban_rural_commune = []
        self.cities = []
        self.delegacy = []

    @classmethod
    def create_county(cls, row_number):
        """
        Creates county with its lists of locations
        :param row_number: int - number of row in csv file
        :return:
        """
        county = cls(Common.file_loaded[row_number][4])
        county_number = Common.file_loaded[row_number][1]
        for row in Common.file_loaded[row_number+1:]:
            if row[1] != county_number:
                break
            if row[3] == '1':
                county.municipality.append(Municipality(row[4]))

            elif row[3] == '2':
                county.rural_commune.append(RuralCommune(row[4]))

            elif row[3] == '3':
                county.urban_rural_commune.append(UrbanRuralCommune(row[4]))

            elif row[3] == '4':
                county.cities.append(City(row[4]))

            elif row[3] == '5':
                county.rural_area.append(RuralArea(row[4]))

            elif row[3] == '9':
                county.delegacy.append(Delegacy(row[4]))

        return county
