from common import Common


class Voivodeship:
    def __init__(self, name, counties):
        self.name = name
        self.counties = counties

    @staticmethod
    def create_voivodeship():
        counties = []
        name = ''
        for row in Common.file_loaded:
            if (row[1], row[2], row[3]) == ('', '', ''):
                name = row[4]
            elif (row[2], row[3]) == ('', ''):
                pass
        return Voivodeship(name, counties)
