from Organism import Organism
import random
import tkinter as tk


class Plant(Organism):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def action(self):

        spread = random.randint(0, 100)
        if spread < 10:
            self.spreading()

    def collision(self, x, y):
        pass

    def collision_ability(self, attacker):
        return True

    def spreading(self):
        x, y = self.get_board().check_if_space(self.get_x(), self.get_y())
        if x == -1 and y == -1:
            return
        else:
            comment = tk.Label(self.get_board().get_window(), text="Spreading" + str(x) + " " + str(y))
            comment.place(x=self.get_board().get_comment_x(), y=self.get_board().get_comment_y(), width=100, height=20)
            self.get_board().get_comments().append(comment)
            self.get_board().set_comment_y(self.get_board().get_comment_y() + 30)
            self.get_board().get_organism().append(self.__class__(self.get_img(), self.get_strength(), self.get_initiative()
                                                              , x, y, self.get_board(), False))
            self.get_board().get_field(x, y).configure(image=self.get_img())
