# importing tkinter module
from tkinter import *
from PIL import ImageTk,Image #image stuff - install package: Pillow


class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger").pack()


        # TODO: liste over personer og deres indbetalinger
        ting = self.master.fodboldtur.items()
        personer = self.master.fodboldtur.keys()
        print(personer)
        '''
        for person in self.master.fodboldtur:
            Label(self.listWindow, text=f'{personer[person]}: {self.master.fodboldtur[personer[person]]},-').pack()
        '''
        for person in self.master.fodboldtur:
            print(personer)

        print(ting)

        print(self.master.fodboldtur.get(1))