from tkinter import *
import firebase as fb
from general import General


class Users(General):

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        self.mini_screen_bg()
        flag = True
        if self.title_name == "Moderators":
            flag = False

        if flag:
            Label(self.root, text="Users", font=("Lucida Grande", 22, "bold"), bg="#2b509c", fg="#f64424") \
                .place(y=50, width=560, height=50)
        else:
            Label(self.root, text="Moderators", font=("Lucida Grande", 22, "bold"), bg="#2b509c", fg="#f64424") \
                .place(y=50, width=560, height=50)

        try:
            if flag:
                parts = fb.db.child("Users").get()
            else:
                parts = fb.db.child("Moderators").get()
            users_name = []
            for n in parts:
                users_name.append(Button(root, text=n.key(), font=("Lucida Grande", 13, "bold"), fg='#fc9d17',
                                         bg='white', borderwidth=5, command=lambda m=n.key(): self.goto_stat(m)))
            padx = 8
            pady = 150
            for b in users_name:
                if padx < 560:
                    if pady < 440:
                        b.place(x=padx, y=pady, width=140, height=50)
                        pady += 58
                    else:
                        pady = 150
                        padx += 202
                        b.place(x=padx, y=pady, width=140, height=50)
                        pady += 58

            back = Button(root, text="⮪", command=self.go_to_admin_menu, font=("Lucida Grande", 20),
                          fg='#f64424', bg='white', borderwidth=5)
            back.place(x=1, y=1, width=80, height=40)

        except Exception:
            self.go_to_admin_menu()
