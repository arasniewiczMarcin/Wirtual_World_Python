from Plant import Plant


class Dandelion(Plant):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def action(self):
        for i in range(3):
            super().action()