from tkinter import *
import firebase as fb
from general import General
import urllib.parse
from PIL import Image, ImageTk
import io


class Admin_Menu(General):
    image = None

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        self.mini_screen_bg()

        Label(self.root, text="Administrator Menu", font=("Lucida Grande", 22, "bold"), bg="#2b509c", fg="#f64424")\
            .place(x=80, y=50, width=400, height=50)
        Button(root, text="Log Out", font=("Lucida Grande", 11, 'bold'), bg="white", fg="#fc9d17",
                         borderwidth=5, command=self.log_out).place(x=470, width=90, height=40)

        parts = fb.db.get()
        list_of_parts = ['Users', 'Moderators']
        buttons = []
        for n in parts:
            if n.key() in list_of_parts:
                buttons.append(Button(root, text=n.key(), font=("Lucida Grande", 13, "bold"), fg='#fc9d17', bg='white',
                    borderwidth=5, command=lambda m=n.key(): self.go_to_choice(m)))
        pady = 0
        for b in buttons:
            b.place(x=8.5, y=150 + pady, width=140, height=50)
            pady += 60


    def go_to_choice(self, name):
        if name == 'Users':
            self.title_name = name
            self.users()

        elif name == 'Moderators':
            self.title_name = name
            self.users()
