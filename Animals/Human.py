from Animal import Animal
import tkinter as tk
import random


class Human(Animal):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)
        self.__directions = {
            "RIGHT": 0,
            "LEFT": 1,
            "DOWN": 2,
            "UP": 3,
            "NONE": 4
        }
        self.__direction = self.__directions["NONE"]
        self.__ability = False
        self.__time_to_end_ability = 5
        self.__time_to_activate_ability = 0

    def get_time_to_end_ability(self):
        return self.__time_to_end_ability

    def set_time_to_end_ability(self, time):
        self.__time_to_end_ability = time

    def get_time_to_activate_ability(self):
        return self.__time_to_activate_ability

    def set_time_to_activate_ability(self, time):
        self.__time_to_activate_ability = time

    def get_ability(self):
        return self.__ability

    def set_ability(self, ability):
        self.__ability = ability

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        self.__direction = self.__directions[direction]

    def get_directions(self):
        return self.__directions

    def action(self):
        counter = 1
        if self.get_ability() is True:
            if 3 <= self.get_time_to_end_ability() <= 5:
                counter = 2
            else:
                rand = random.randint(0, 100)
                if rand < 50:
                    counter = 1
                else:
                    counter = 2
        else:
            counter = 1

        for i in range(counter):
            if self.get_direction() == self.get_directions()["NONE"]:
                return
            x = self.get_x() + self.create_vector(self.get_direction())[0]
            y = self.get_y() + self.create_vector(self.get_direction())[1]
            if self.get_board().check_if_on_map(x, y) is False:
                return
            if self.get_board().checkIfFieldIsOccupied(x, y):
                self.collision(x, y)
            else:
                self.make_move(x, y)
        self.set_direction("NONE")
        self.move_info = tk.Label(self.get_board().get_window(), text="Make your move", bg='black', fg='white', font=("Helvetica", 10))
        self.move_info.place(x=int(self.get_board().get_sizeX()) * 40 + 10, y=60, width=100, height=30)

        if self.get_ability() is True:
            self.set_time_to_end_ability(self.get_time_to_end_ability() - 1)
            if self.get_time_to_end_ability() == 0:
                self.set_ability(False)
                self.set_time_to_activate_ability(5)
        else:
            if self.get_time_to_activate_ability() > 0:
                self.set_time_to_activate_ability(self.get_time_to_activate_ability() - 1)

    def activate_ability(self):
        if self.get_ability() is False and self.get_time_to_activate_ability() == 0:
            self.set_ability(True)
            self.set_time_to_activate_ability(5)
            self.set_time_to_end_ability(5)


