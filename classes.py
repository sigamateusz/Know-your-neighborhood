class Location:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def get_kind(self):
        return self.kind

    def get_name(self):
        return self.name


class City(Location):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class UrbanRuralCommune(Location):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class RuralCommune(Location):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class RuralArea(Location):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class Municipality(Location):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class Delegacy(Location):
    def __init__(self, name, kind):
        super().__init__(name, kind)
