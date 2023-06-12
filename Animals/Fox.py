from Animal import Animal


class Fox(Animal):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def action(self):
        x, y = self.rand_direction()
        if self.get_board().checkIfFieldIsOccupied(x, y):
            if self.get_board().get_organism_on_field(x, y).get_strength() <= self.get_strength():
                self.collision(x, y)
        else:
            self.make_move(x, y)

