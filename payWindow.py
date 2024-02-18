# importing tkinter module
from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")
        self.fodboldtur = master.fodboldtur
        self.subject = 0
        self.clicked = StringVar()
        self.currentPayer = 'Hans Hansen'
        self.clicked.set('Personer')


        self.label = Label(self.payWindow,
                           text=f'Indbetal for {self.currentPayer}')
        self.label.pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

        self.spacer = Label(self.payWindow)
        self.spacer.pack()

        Label(self.payWindow,
              text="Vælg person:").pack()

        # TODONE: Dropdown for personer
        self.drop = OptionMenu(self.payWindow, self.clicked, *self.fodboldtur)
        self.drop.pack()

        # Create button, it will change label text
        self.button = Button(self.payWindow, text="bekræft", command=self.show).pack()


        #Label(self.payWindow,
        #      text=f'Indbetaler for: {fodboldtur[self.subject[0]]}')

        '''
        for item in fodboldtur.items():
            print(f'{item[0]}s indbetalings-data:')
            self.person = Button(self.payWindow, text=f'{item[0]}', command= self.currentPayer(item[0]))
            self.person.pack()
        '''


        self.payWindow.mainloop()

    def addMoney(self):
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        self.master.fodboldtur[self.currentPayer] += amount
        self.master.total = sum(self.master.fodboldtur.values())
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100

        print(self.master.fodboldtur)
        print(self.master.total)
        print(sum(self.master.fodboldtur.values()))

    # Change the label text
    def show(self):
        self.label.config(text=f'Indbetal for {self.clicked.get()}')
        self.currentPayer = self.clicked.get()
