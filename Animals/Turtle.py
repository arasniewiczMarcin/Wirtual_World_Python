from Animal import Animal
import random


class Turtle(Animal):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def action(self):
        turtle_move = random.randint(0, 100)
        if turtle_move < 25:
            super(Turtle, self).action()

    def collision_ability(self, attacker):
        if attacker.get_strength() < 5:
            return False
        else:
            return True
