# importing tkinter module
from tkinter import *
from tkinter.ttk import * #progressbar
import pickle
import random

from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass


class mainWindow:
    def __init__(self):
        self.filename = 'betalinger.pk'
        self.fodboldtur = {}
        self.personbeløb = 4500
        self.infile = open(self.filename, 'rb')
        self.fodboldtur = pickle.load(self.infile)
        self.infile.close()
        self.total = sum(self.fodboldtur.values())
        self.target = self.personbeløb * len(self.fodboldtur)
        # creating tkinter window
        self.root = Tk()

        for item in self.fodboldtur.items():
            print(item[0])
            print(item[1])
            print(self.fodboldtur[item[0]])
            print(self.fodboldtur[item[0]])

        print(self.fodboldtur.values())

        print(self.fodboldtur)

        print(self.fodboldtur['Ole Olsen'])


        #TEXT

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient = HORIZONTAL,
                    length = 250, mode = 'determinate')
        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])
        #BUTTONS
        self.progress.pack(padx= 20)

        listButton = Button(self.root,text ="Liste over indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 10,side=LEFT)

        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        bottom3Button = Button(self.root,text ="Administration",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop
        mainloop()

if __name__ == '__main__':
    main = mainWindow()


# Øhm links:
# https://stackoverflow.com/questions/4880960/how-to-sum-all-the-values-in-a-dictionary
# https://www.geeksforgeeks.org/dropdown-menus-tkinter/
# https://docs.python.org/3/library/tkinter.html
# https://note.nkmk.me/en/python-dict-clear-pop-popitem-del/
# https://docs.python.org/3/tutorial/errors.html
# https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/
# https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/
# https://github.com/Robotto/fodboldGUI/blob/master/payWindow.py
#
#
#
#
#
#
#
#
#

