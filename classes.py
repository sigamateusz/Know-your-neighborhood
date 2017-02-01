class City:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class UrbanRuralCommune(City):
    def __init__(self, name):
        super().__init__(name)


class RuralCommune(City):
    def __init__(self, name):
        super().__init__(name)


class RuralArea(City):
    def __init__(self, name):
        super().__init__(name)


class Municipality(City):
    def __init__(self, name):
        super().__init__(name)


class Delegacy(City):
    def __init__(self, name):
        super().__init__(name)
