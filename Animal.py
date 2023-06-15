from Organism import Organism
import tkinter as tk


class Animal(Organism):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def action(self):
        x, y = self.rand_direction()
        if self.get_board().checkIfFieldIsOccupied(x, y):
            self.collision(x, y)
        else:
            self.make_move(x, y)

    def collision(self, x, y):
        if str(self.get_board().get_field(x, y).cget("image")) == str(self.get_img()):
            self.breeding(x, y)
        else:
            self.fight(self.get_board().get_organism_on_field(x, y))

    def collision_ability(self, attacker):
        return True

    def make_move(self, x, y):
        self.get_board().get_field(self.get_x(), self.get_y()).configure(bg="gray", image="")
        self.set_x(x)
        self.set_y(y)
        self.get_board().get_field(x, y).configure(image=self.get_img())

    def breeding(self, x, y):
        comment = tk.Label(self.get_board().get_window(), text="breeding" + str(x) + " " + str(y))
        comment.place(x = self.get_board().get_comment_x(), y = self.get_board().get_comment_y(), width=100, height=20)
        self.get_board().get_comments().append(comment)
        self.get_board().set_comment_y(self.get_board().get_comment_y() + 30)

        self.set_move(False)
        if self.get_board().get_organism_on_field(x, y) is not None:
            self.get_board().get_organism_on_field(x, y).set_move(False)
        position = self.get_board().check_if_space(x, y)
        if position[0] != -1 and position[1] != -1:
            self.get_board().get_organism().append(self.__class__(self.get_img(), self.get_strength(), self.get_initiative(), position[0], position[1], self.get_board(), False))
            self.get_board().get_field(position[0], position[1]).configure(image=self.get_img())

    def fight(self, defender):
        comment = tk.Label(self.get_board().get_window(), text="fight" + str(defender.get_x()) + " " + str(defender.get_y()))
        comment.place(x=self.get_board().get_comment_x(), y=self.get_board().get_comment_y(), width=100, height=20)
        self.get_board().get_comments().append(comment)
        self.get_board().set_comment_y(self.get_board().get_comment_y() + 30)

        if defender is not None:
            if defender.collision_ability(self):
                if self.get_strength() >= defender.get_strength():
                    self.get_board().get_field(defender.get_x(), defender.get_y()).configure(bg="gray", image="")
                    if defender in self.get_board().get_organism():
                        self.get_board().get_organism().remove(defender)
                    self.make_move(defender.get_x(), defender.get_y())
                else:
                    self.get_board().get_field(self.get_x(), self.get_y()).configure(bg="gray", image="")
                    if self in self.get_board().get_organism():
                        self.get_board().get_organism().remove(self)





