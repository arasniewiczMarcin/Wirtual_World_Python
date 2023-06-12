from Animal import Animal
import random

class Antelope(Animal):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def action(self):
        super(Antelope, self).action()
        super(Antelope, self).action()

    def collision_ability(self, attacker):
        run = random.randint(0, 100)
        if run < 50:
            x, y = self.get_board().check_if_space(self.get_x(), self.get_y())
            if x != -1 and y != -1:
                self.get_board().get_field(self.get_x(), self.get_y()).configure(bg="gray", image="")
                self.set_x(x)
                self.set_y(y)
                self.get_board().get_field(x, y).configure(image=self.get_img())
            return False
        else:
            return True