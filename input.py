import tkinter as tk


class Input:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wirtual World")

        photo = tk.PhotoImage(file="images/Enter.png")
        tk.Label(self.window, image=photo).grid(row=0, column=0)
        self.entryHeight = tk.Entry(self.window, width=10, bg= 'white', font=("Arial", 22), border=0)
        self.entryHeight.place(x=50, y=84)
        self.entryWidth = tk.Entry(self.window, width=10, bg= 'white', font=("Arial", 22), border=0)
        self.entryWidth.place(x=320, y=84)
        tk.Button(self.window, text="Submit", command= self.send_input).place(x=200, y=130, width=100, height=30)

        self.window.mainloop()

    def send_input(self):
        if self.entryHeight.get() == "" or self.entryWidth.get() == "" or int(self.entryHeight.get()) > 25 or int(self.entryWidth.get()) > 30:
            return
        self.sizeX = self.entryWidth.get()
        self.sizeY = self.entryHeight.get()
        self.window.destroy()
