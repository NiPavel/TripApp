from tkinter import *
from tkinter import messagebox
import firebase as fb
from general import General
from datetime import date


class Pictures(General):
    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)

        Label(self.root, text=self.pname, font=("Cambria", 20, 'italic')).place(x=500, y=10)
        self.count = None
        parts = fb.db.child("Counter").get()
        for n in parts:
            if self.pname == n.key():
                self.count = n.val()
            else:
                self.count = 0

        key = Label(self.root, text='Enter a path to a picture:', font=("Times New Roman", 18, 'bold'),
                    bg='grey')
        key.place(x=0, y=100)

        key_ent = Entry(self.root, width=50, fg="black", bd=5)
        key_ent.place(x=360, y=90, height=50)

        add = Button(self.root, text="Add", borderwidth=5, command=lambda: self.do_add(key_ent.get()), width=20)
        add.place(x=680, y=280)

        back = Button(self.root, text="<<", borderwidth=5, command=lambda: self.deletePart("Pictures"), width=20)
        back.grid(row=0, column=0, stick='we')

    def do_add(self, path_pc):
        self.count += 1
        path_fb = "images/{0}/{1}/".format(self.cname, self.pname) + str(self.count) + ".jpg"
        flag = True
        try:
            fb.storage.child(path_fb).put(path_pc)
        except Exception:
            flag = False
            messagebox.showerror("Error!", "Something went wrong!")

        if flag:
            today = date.today()
            fb.db.child("Moderators").child(self.uname).child("Work").child("Add Picture").update(
                {self.pname: "Added a picture at " + str(today)})
            messagebox.showinfo("Successful", "You have added a picture to a " + self.pname)
            fb.db.child("Counter").update({self.pname: self.count})
