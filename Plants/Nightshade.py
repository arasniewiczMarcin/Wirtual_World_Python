from Plant import Plant


class Nightshade(Plant):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def collision_ability(self, attacker):
        attacker.set_strength(0)
        return True
