import tkinter as tk


class Input:
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("Wirtual World")

        photo = tk.PhotoImage(file="images/Enter.png")
        tk.Label(self.__window, image=photo).grid(row=0, column=0)
        self.__entryHeight = tk.Entry(self.__window, width=10, bg='white', font=("Arial", 22), border=0)
        self.__entryHeight.place(x=50, y=84)
        self.__entryWidth = tk.Entry(self.__window, width=10, bg='white', font=("Arial", 22), border=0)
        self.__entryWidth.place(x=320, y=84)
        tk.Button(self.__window, text="Submit", command= self.send_input).place(x=200, y=130, width=100, height=30)

        self.__sizeX = ""
        self.__sizeY = ""

        self.__window.mainloop()

    def send_input(self):
        if self.__entryHeight.get() == "" or self.__entryWidth.get() == "" or int(self.__entryHeight.get()) > 25 or int(self.__entryWidth.get()) > 30:
            return
        self.set_size_x(self.__entryWidth.get())
        self.set_size_y(self.__entryHeight.get())
        self.__window.destroy()

    def set_size_x(self, size_x):
         self.__sizeX = size_x

    def set_size_y(self, size_y):
        self.__sizeY = size_y

    def get_size_x(self):
        return self.__sizeX

    def get_size_y(self):
        return self.__sizeY

