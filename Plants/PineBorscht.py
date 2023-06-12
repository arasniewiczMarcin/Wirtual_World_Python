from Plant import Plant


class PineBorscht(Plant):
    def __init__(self, img, strength, initiative, x, y, board, move):
        super().__init__(img, strength, initiative, x, y, board, move)

    def action(self):
        super().action()
        self.kill_animals_around()

    def kill_animals_around(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.get_board().check_if_on_map(self.get_x() + j, self.get_y() + i) and self.get_board().checkIfFieldIsOccupied(self.get_x() + j, self.get_y() + i):

                    org = self.get_board().get_organism_on_field(self.get_x() + j, self.get_y() + i)
                    if org is not None and org.get_initiative() > 0 and org.get_img() != self.get_board().get_images()["CyberSheep"]:
                        self.get_board().get_organism().remove(org)
                        self.get_board().get_field(self.get_x() + j, self.get_y() + i).configure(image="")

    def collision_ability(self, attacker):
        if str(attacker.get_img()) != str(self.get_board().get_images()["CyberSheep"]):
            print(str(attacker.get_img()) + " " + str(self.get_board().get_images()["CyberSheep"]))
            attacker.set_strength(0)
        return True


