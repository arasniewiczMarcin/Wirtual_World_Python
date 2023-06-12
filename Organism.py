from abc import ABC, abstractmethod
import random


class Organism(ABC):
    def __init__(self, img, strength, initiative, x, y, board, move):
        self.img = img
        self.strength = strength
        self.initiative = initiative
        self.x = x
        self.y = y
        self.board = board
        self.move = move

    def get_img(self):
        return self.img

    def get_strength(self):
        return self.strength

    def get_initiative(self):
        return self.initiative

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_board(self):
        return self.board

    def get_move(self):
        return self.move

    def set_img(self, img):
        self.img = img

    def set_strength(self, strength):
        self.strength = strength

    def set_initiative(self, initiative):
        self.initiative = initiative

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_board(self, board):
        self.board = board

    def set_move(self, move):
        self.move = move

    def rand_direction(self):
        while True:
            direction = random.randint(0, 3)
            vector = self.create_vector(direction)
            new_x = int(self.get_x()) + int(vector[0])
            new_y = int(self.get_y()) + int(vector[1])
            if 0 <= int(new_x) < int(self.get_board().get_sizeX()) and 0 <= int(new_y) < int(self.get_board().get_sizeY()):
                break

        return new_x, new_y

    def create_vector(self, direction):
        vector = [0, 0]
        # 0 - right
        if direction == 0:
            vector[0] = 1
        # 1 - left
        elif direction == 1:
            vector[0] = -1
        # 2 - down
        elif direction == 2:
            vector[1] = 1
        # 3 - up
        elif direction == 3:
            vector[1] = -1
        return vector


    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, x, y):
        pass

    @abstractmethod
    def collision_ability(self, attacker):
        pass

    # virtual void akcja(Swiat* swiat) = 0;
	# virtual void kolizja(Swiat* swiat, Polozenie miejsceKolizji) = 0;
	# virtual bool umiejetnoscKolizja(Organizm* atakujacy, string& komentarz);


