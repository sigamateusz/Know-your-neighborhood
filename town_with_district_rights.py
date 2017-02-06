from county import County


class TownWithDistrictRights(County):

    def __init__(self, name):
        super().__init__(name, 'miasto na prawach powiatu')
