# importing tkinter module
from tkinter import *
from tkinter import messagebox


class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Administration")
        self.worstWindow.geometry("200x300")
        self.clicked = StringVar()
        self.removing = ''
        self.clicked.set('Personer')

        # TODONE: Tilføjelse af ny person
        Label(self.worstWindow, text="Tilføj ny person").pack()
        self.nyPerson = Entry(self.worstWindow).pack()
        self.button = Button(self.worstWindow, text="Tilføj", command=self.addPerson).pack()

        self.spacer = Label(self.worstWindow).pack()

        # TODONE: Fjernelse af person
        Label(self.worstWindow, text="Fjern person").pack()
        self.drop = OptionMenu(self.worstWindow, self.clicked, *self.master.fodboldtur).pack()
        self.button = Button(self.worstWindow, text="Fjern", command=self.removePerson).pack()

        self.spacer = Label(self.worstWindow).pack()

        # TODONE: Ændring af krævede beløb pr. person
        self.beløbTitel = Label(self.worstWindow, text=f'Ændr personbeløb:\nNuværende: {self.master.personbeløb},-')
        self.beløbTitel.pack()
        self.nytPersonbeløb = Entry(self.worstWindow)
        self.nytPersonbeløb.pack()
        self.button = Button(self.worstWindow, text="Bekræft", command=self.changePersonbeløb).pack()

        self.worstWindow.mainloop()


    def addPerson(self):
        person = str(self.nyPerson.get())
        if person in self.master.fodboldtur:
            messagebox.showerror(parent=self.worstWindow, title="Person eksisterer allerede!", message="Prøv igen.\nSkriv et nyt navn!")
            return
        else:
            try:
                person = str(self.nyPerson.get())  # HUSK AT VALIDERE INPUT!, kun string!
            except:
                messagebox.showerror(parent=self.worstWindow, title="Fejl i navn!", message="Prøv igen.\nKun hele tal!")
                return

            self.master.fodboldtur.update({person: 0})
            print(f"Tilføjet: {person} til personer: {self.master.fodboldtur}")


    def removePerson(self):
        try:
            del self.master.fodboldtur[self.clicked.get()]
            print(self.master.fodboldtur)
        except:
            messagebox.showerror(parent=self.worstWindow, title="Person eksisterer ikke!", message="Prøv igen.\nVælg en anden person!")


    def changePersonbeløb(self):
        try:
            nytBeløb = abs(int(self.nytPersonbeløb.get()))  # HUSK AT VALIDERE INPUT!, kun string!
            self.master.personbeløb = nytBeløb
        except Exception as inst:
            messagebox.showwarning(parent=self.worstWindow, title="Fejl i beløb!", message="Prøv igen.\nKun hele tal!")
            return

        self.master.target = self.master.personbeløb * len(self.master.fodboldtur)
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        self.master.progress['value'] = self.master.total / self.master.target * 100

        print(self.master.total)
        print(self.master.target)

        self.beløbTitel.config(text=f'Ændr personbeløb:\nNuværende: {self.master.personbeløb},-')


