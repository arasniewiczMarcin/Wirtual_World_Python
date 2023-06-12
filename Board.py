import random
import tkinter as tk
from Animals.Antelope import Antelope
from Animals.CyberSheep import CyberSheep
from Animals.Fox import Fox
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Animals.Human import Human
from Animals.Sheep import Sheep
from Plants.Nightshade import Nightshade
from Plants.PineBorscht import PineBorscht
from Animals.Turtle import Turtle
from Animals.Wolf import Wolf


class Board:
    def __init__(self, sizeX, sizeY):

        self.sizeX = sizeX
        self.sizeY = sizeY
        self.comment_x = int(sizeX) * 40 + 30
        self.comment_y = 210

        self.comments = []

        self.window = tk.Tk()
        self.window.title("Wirtual World")
        self.window.configure(background='green')
        self.window.geometry(str(int(sizeX) * 60) + "x" + str(int(sizeY) * 40))
        self.next_turn_btn = tk.Button(self.window, text="Next turn", command=self.next_turn)
        self.next_turn_btn.place(x=int(sizeX) * 40 + 10, y=10, width=100, height=30)
        self.window.resizable(False, False)
        self.organisms = []
        self.x = 0
        self.y = 0

        self.images = {
            "Antelope": tk.PhotoImage(file="images/antylopa.png"),
            "CyberSheep": tk.PhotoImage(file="images/cyberowca.png"),
            "Fox": tk.PhotoImage(file="images/lis.png"),
            "Grass": tk.PhotoImage(file="images/trawa.png"),
            "Guarana": tk.PhotoImage(file="images/guarana.png"),
            "Human": tk.PhotoImage(file="images/czlowiek.png"),
            "Sheep": tk.PhotoImage(file="images/owca.png"),
            "Nightshade": tk.PhotoImage(file="images/wilczeJagody.png"),
            "PineBorscht": tk.PhotoImage(file="images/barszcz.png"),
            "Turtle": tk.PhotoImage(file="images/zolw.png"),
            "Wolf": tk.PhotoImage(file="images/wilk.png"),
        }
        
        self.map = [[[] for _ in range(int(self.sizeY))] for _ in range(int(self.sizeX))]

        for i in range(int(self.sizeX)):
            for j in range(int(self.sizeY)):
                if (int(i) + int(j)) % 2 == 0:
                    self.map[i][j] = tk.Label(self.window, bg='gray', border=0)
                else:
                    self.map[i][j] = tk.Label(self.window, bg='gray', border=0)
                self.map[i][j].place(x=i * 40 + 5, y=j * 40 + 5, width=30, height=30)

        self.organisms_num = int(int(self.sizeX) * int(self.sizeY) * 0.01) + 1

        self.drawXY()
        self.organisms.append(Human(self.images["Human"], 4, 4, self.x, self.y, self, 1))
        self.human = self.organisms[0]

        for i in range(self.organisms_num):
            self.drawXY()
            self.organisms.append(Antelope(self.images["Antelope"], 4, 4, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(CyberSheep(self.images["CyberSheep"], 11, 4, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(Fox(self.images["Fox"], 3, 7, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(Grass(self.images["Grass"], 0, 0, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(Guarana(self.images["Guarana"], 0, 0, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(Sheep(self.images["Sheep"], 4, 4, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(Nightshade(self.images["Nightshade"], 99, 0, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(PineBorscht(self.images["PineBorscht"], 10, 0, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(Turtle(self.images["Turtle"], 2, 1, self.x, self.y, self, 1))
            self.drawXY()
            self.organisms.append(Wolf(self.images["Wolf"], 9, 5, self.x, self.y, self, 1))

        if self.human.get_direction() == self.human.get_directions()["NONE"]:
            self.move_info = tk.Label(self.window, text="Make your move", bg='black', fg='white', font=("Helvetica", 10))
        else:
            self.move_info = tk.Label(self.window, text="Moved choosen", bg='black', fg='white', font=("Helvetica", 10))

        self.move_info.place(x=int(self.get_sizeX()) * 40 + 10, y=60, width=100, height=30)

        self.ability_info = tk.Label(self.window, text="Press A to activate ability", bg='black', fg='white', font=("Helvetica", 10))
        self.ability_info.place(x=int(self.get_sizeX()) * 40 + 10, y=100, width=150, height=30)

        self.save_info = tk.Label(self.window, text="Press s to save", bg='black', fg='white',
                                     font=("Helvetica", 10))
        self.save_info.place(x=int(self.get_sizeX()) * 40 + 10, y=140, width=150, height=30)

        self.save_info = tk.Label(self.window, text="Press l to load", bg='black', fg='white',
                                  font=("Helvetica", 10))
        self.save_info.place(x=int(self.get_sizeX()) * 40 + 10, y=170, width=150, height=30)

        self.window.bind("<a>", lambda event: self.human.activate_ability())
        self.window.bind("<s>", lambda event: self.save())
        self.window.bind("<l>", lambda event: self.load())
        self.window.bind("<Up>", lambda event: self.make_move("UP"))
        self.window.bind("<Down>", lambda event:  self.make_move("DOWN"))
        self.window.bind("<Left>", lambda event:  self.make_move("LEFT"))
        self.window.bind("<Right>", lambda event:  self.make_move("RIGHT"))

        self.draw_organisms()
        self.window.mainloop()

    def get_comments(self):
        return self.comments

    def get_comment_x(self):
        return self.comment_x

    def get_comment_y(self):
        return self.comment_y

    def set_comment_x(self, x):
        self.comment_x = x

    def set_comment_y(self, y):
        self.comment_y = y

    def set_human(self, human):
        self.human = human

    def make_move(self, direction):
        self.human.set_direction(direction)
        if self.human.get_direction() != self.human.get_directions()["NONE"]:
            self.move_info = tk.Label(self.window, text="Move choosen", bg='black', fg='white', font=("Helvetica", 10))
            self.move_info.place(x=int(self.get_sizeX()) * 40 + 10, y=60, width=100, height=30)

    def get_sizeX(self):
        return self.sizeX

    def get_window(self):
        return self.window

    def get_sizeY(self):
        return self.sizeY

    def get_map(self):
        return self.map

    def get_organism(self):
        return self.organisms

    def get_images(self):
        return self.images

    def get_field(self, x, y):
        return self.map[x][y]

    def set_sizeX(self, sizeX):
        self.sizeX = sizeX

    def set_sizeY(self, sizeY):
        self.sizeY = sizeY

    def set_map(self, map):
        self.map = map

    def set_organism(self, organisms):
        self.organisms = organisms

    def set_images(self, images):
        self.images = images

    def set_field(self, x, y, field):
        self.map[x][y] = field

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def checkIfFieldIsOccupied(self, x, y):
        if self.get_field(x, y).cget("image") == "":
            return False
        else:
            return True

    def drawXY(self):
        x = random.randint(0, int(self.sizeX) - 1)
        y = random.randint(0, int(self.sizeY) - 1)
        while self.checkIfFieldIsOccupied(x, y):
            x = random.randint(0, int(self.sizeX) - 1)
            y = random.randint(0, int(self.sizeY) - 1)

        self.set_x(x)
        self.set_y(y)

    def draw_organisms(self):
        for organism in self.get_organism():
            self.get_field(organism.get_x(), organism.get_y()).configure(image=organism.get_img())

    def next_turn(self):
        for comment in self.get_comments():
            comment.destroy()
        self.get_comments().clear()
        self.set_comment_y(210)
        if self.human.get_direction() != self.human.get_directions()["NONE"]:
            max_initiative = int(7)
            for i in range(max_initiative, -1, -1):
                for organism in self.get_organism():
                    if int(organism.get_initiative()) == i and organism.get_move():
                        organism.action()

            for organism in self.get_organism():
                organism.set_move(True)

    def get_human(self):
        return self.human

    def get_organism_on_field(self, x, y):
        for organism in self.get_organism():
            if organism.get_x() == x and organism.get_y() == y:
                return organism
        return None

    def check_if_space(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + j < int(self.sizeX) and 0 <= y + i < int(self.sizeY) and not self.checkIfFieldIsOccupied(x + j, y + i):
                    return x + j, y + i
        return -1, -1

    def check_if_on_map(self, x, y):
        if 0 <= x < int(self.sizeX) and 0 <= y < int(self.sizeY):
            return True
        return False

    def save(self):
        file = open("save.txt", "w")
        file.write(str(self.get_sizeX()) + " " + str(self.get_sizeY()) + " " + str(self.get_human().get_ability()) +
                   " "+ str(self.get_human().get_time_to_activate_ability()) + " " + str(self.get_human().get_time_to_end_ability()) + "\n")
        for organism in self.get_organism():
            file.write(str(organism.get_img())+ " " + str(organism.get_strength()) + " " + str(organism.get_initiative()) +
                       " " + str(organism.get_x()) + " " + str(organism.get_y())  + " " + " " + str(organism.get_move()) + "\n")

    def load(self):
        file = open("save.txt", "r")
        counter = 0
        for widget in self.get_window().winfo_children():
            widget.destroy()
        self.get_organism().clear()

        ability = False
        time_to_activate_ability = 0
        time_to_end_ability = 5

        for line in file:
            counter += 1
            if counter == 1:
                self.set_sizeX(int(line.split(" ")[0]))
                self.set_sizeY(int(line.split(" ")[1]))
                ability = line.split(" ")[2]
                time_to_activate_ability = line.split(" ")[3]
                time_to_end_ability = line.split(" ")[4]
            else:
                self.load_organism(line.split(" ")[0], line.split(" ")[1], line.split(" ")[2], line.split(" ")[3], line.split(" ")[4], line.split(" ")[5])

        if self.get_organism()[0].get_img() == "pyimage7":
            self.set_human(self.get_organism()[0])
            self.get_human().set_ability(bool(ability))
            self.get_human().set_time_to_activate_ability(int(time_to_activate_ability))
            self.get_human().set_time_to_end_ability(int(time_to_end_ability))

        self.window.title("Wirtual World")
        self.window.configure(background='green')
        self.window.geometry(str(int(self.get_sizeX()) * 60) + "x" + str(int(self.get_sizeY()) * 40))
        self.next_turn_btn = tk.Button(self.window, text="Next turn", command=self.next_turn)
        self.next_turn_btn.place(x=int(self.get_sizeX()) * 40 + 10, y=10, width=100, height=30)
        self.window.resizable(False, False)

        if self.human.get_direction() == self.human.get_directions()["NONE"]:
            self.move_info = tk.Label(self.window, text="Make your move", bg='black', fg='white', font=("Helvetica", 10))
        else:
            self.move_info = tk.Label(self.window, text="Moved choosen", bg='black', fg='white', font=("Helvetica", 10))

        self.move_info.place(x=int(self.get_sizeX()) * 40 + 10, y=60, width=100, height=30)

        self.ability_info = tk.Label(self.window, text="Press A to activate ability", bg='black', fg='white', font=("Helvetica", 10))
        self.ability_info.place(x=int(self.get_sizeX()) * 40 + 10, y=100, width=150, height=30)

        self.save_info = tk.Label(self.window, text="Press s to save", bg='black', fg='white',
                                     font=("Helvetica", 10))
        self.save_info.place(x=int(self.get_sizeX()) * 40 + 10, y=140, width=150, height=30)

        self.save_info = tk.Label(self.window, text="Press l to load", bg='black', fg='white',
                                  font=("Helvetica", 10))
        self.save_info.place(x=int(self.get_sizeX()) * 40 + 10, y=170, width=150, height=30)

        self.map = [[[] for _ in range(int(self.sizeY))] for _ in range(int(self.sizeX))]

        for i in range(int(self.get_sizeY())):
            for j in range(int(self.get_sizeX())):
                if (int(i) + int(j)) % 2 == 0:
                    self.map[i][j] = tk.Label(self.window, bg='gray', border=0)
                else:
                    self.map[i][j] = tk.Label(self.window, bg='gray', border=0)
                self.map[i][j].place(x=i * 40 + 5, y=j * 40 + 5, width=30, height=30)

        self.set_comment_x(int(self.get_sizeX()) * 40 + 10)

        self.draw_organisms()
        self.window.mainloop()

        file.close()

    def load_organism(self, image, s, ini, x, y, move):
        image_mapping = {
            "pyimage12": Wolf,
            "pyimage11": Turtle,
            "pyimage2": Antelope,
            "pyimage3": CyberSheep,
            "pyimage4": Fox,
            "pyimage5": Grass,
            "pyimage6": Guarana,
            "pyimage7": Human,
            "pyimage8": Sheep,
            "pyimage9": Nightshade,
            "pyimage10": PineBorscht
        }

        organism_class = image_mapping.get(image)
        if organism_class:
            self.get_organism().append(organism_class(image, int(s), int(ini), int(x), int(y), self, move))




