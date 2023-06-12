from Plant import Plant


class Guarana(Plant):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def collision_ability(self, attacker):
        attacker.set_strength(attacker.get_strength() + 3)
        return True
