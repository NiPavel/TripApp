from tkinter import *
from tkinter import messagebox
from general import General
import firebase as fb


class deletePart(General):
    name = None

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind, name):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        self.name = name

        Label(self.root, text=self.name + " of the " + self.cname, font=("Cambria", 20, 'italic')).place(x=500, y=10)

        parts = fb.db.child('Cities').child(self.cname).child(self.name).get()
        part_list = []

        for n in parts:
            k = n.key()
            v = n.val()
            part_list.append(Button(self.root, text=k + ':' + v, borderwidth=5,
                                    command=lambda m=k: self.goto_charge(self.ind, m)))

        grid_count = 0
        for g in part_list:
            g.grid(row=1 + grid_count, column=0, stick='we', padx=20, pady=20)
            grid_count += 1

        back = Button(self.root, text="<<", borderwidth=5, command=self.go_to_parts, width=20)
        back.grid(row=0, column=0, stick='we')
