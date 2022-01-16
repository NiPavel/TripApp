from tkinter import *
from tkinter import messagebox
from general import General
import firebase as fb
from datetime import date


class addPart(General):

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind, name):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        self.name = name

        Label(self.root, text=name + " of the " + self.cname, font=("Cambria", 20, 'italic')).place(x=500, y=10)


        key = Label(self.root, text='Enter name of ' + self.name[:-1] + ':', font=("Times New Roman", 18, 'bold'),
                    bg='grey')
        key.place(x=0, y=100)

        key_ent = Entry(self.root, width=50, fg="blue", justify=CENTER, bd=5)
        key_ent.place(x=360, y=90, height=50)

        value = Label(self.root, text='Enter price of ' + self.name[:-1] + ':', font=("Times New Roman", 18, 'bold'),
                      bg='grey')
        value.place(x=0, y=200)

        value_ent = Entry(self.root, width=50, fg="blue", justify=CENTER, bd=5)
        value_ent.place(x=360, y=190, height=50)

        add = Button(self.root, text="Add", borderwidth=5, command=lambda: self.do_add(key_ent.get(), value_ent.get()),
                     width=20)
        add.place(x=680, y=280)

        back = Button(self.root, text="<<", borderwidth=5, command=self.go_to_parts, width=20)
        back.grid(row=0, column=0, stick='we')



    def do_add(self, name, price):
        if len(price) == 0 or len(name) == 0 or price[0] != '₪' or price[1:].isnumeric() == False or price == None:
            messagebox.showwarning("Wrong input!", "Please input a correct price")
        else:
            today = date.today()
            fb.db.child("Moderators").child(self.uname).child("Work").child("Add Place").update(
                {name: "Added at " + str(today)})
            fb.db.child("Cities").child(self.cname).child(self.name).update({name: price})
            messagebox.showinfo("Successful", "You have added a " + name)
