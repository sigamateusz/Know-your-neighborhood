class City:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def get_kind(self):
        return self.kind

    def get_name(self):
        return self.name


class UrbanRuralCommune(City):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class RuralCommune(City):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class RuralArea(City):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class Municipality(City):
    def __init__(self, name, kind):
        super().__init__(name, kind)


class Delegacy(City):
    def __init__(self, name, kind):
        super().__init__(name, kind)
