from Animal import Animal


class CyberSheep(Animal):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def find_nearest_pine_borscht(self):
        x = -1
        y = -1
        distance = 1000
        for organism in self.get_board().get_organism():
            if organism.get_img() == self.get_board().get_images()["PineBorscht"]:
                if x == -1 or y == -1 or distance > self.count_distance(organism.get_x(), organism.get_y()):
                    distance = self.count_distance(organism.get_x(), organism.get_y())
                    x, y = organism.get_x(), organism.get_y()

        return x, y

    def count_distance(self, x, y):
        return abs(self.get_x() - x) + abs(self.get_y() - y)

    def action(self):
        x, y = self.find_nearest_pine_borscht()
        if x == -1 and y == -1:
            super(CyberSheep, self).action()
        else:
            x_cyber = self.get_x()
            y_cyber = self.get_y()
            if x > self.get_x():
                x_cyber = self.get_x() + 1
            elif x < self.get_x():
                x_cyber = self.get_x() - 1
            elif y > self.get_y():
                y_cyber = self.get_y() + 1
            else:
                y_cyber = self.get_y() - 1

            if self.get_board().checkIfFieldIsOccupied(x_cyber, y_cyber):
                self.collision(x_cyber, y_cyber)
            else:
                self.make_move(x_cyber, y_cyber)