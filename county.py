from common import Common


class County:
    def __init__(self, name):
        self.name = name
        self.delegacy = []
        self.municipality = []
        self.town_with_district_rights = []
        self.rural_area = []
        self.rural_commune = []
        self.urban_rural_commune = []
        self.cities = []

    @classmethod
    def create_county(cls, row_number):
        county = cls(Common.file_loaded[row_number][4])

        return county

    def __str__(self):
        return self.name
