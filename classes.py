class Location:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def get_kind(self):
        return self.kind

    def get_name(self):
        return self.name


class City(Location):
    def __init__(self, name):
        super().__init__(name, 'miasto')


class UrbanRuralCommune(Location):
    def __init__(self, name):
        super().__init__(name, 'gmina miejsko - wiejska')


class RuralCommune(Location):
    def __init__(self, name):
        super().__init__(name, 'gmina wiejska')


class RuralArea(Location):
    def __init__(self, name):
        super().__init__(name, 'obszar wiejski')


class Municipality(Location):
    def __init__(self, name):
        super().__init__(name, 'gmina miejska')


class Delegacy(Location):
    def __init__(self, name):
        super().__init__(name, 'delegatura')
