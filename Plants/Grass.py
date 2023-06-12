from Plant import Plant


class Grass(Plant):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

