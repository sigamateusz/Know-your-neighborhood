from county import County


class TownWithDistrictRights(County):

    def __init__(self, name, kind):
        super().__init__(name, kind)
