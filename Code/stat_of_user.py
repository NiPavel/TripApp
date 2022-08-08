from tkinter import *
import firebase as fb
from general import General
import fa
from tkinter import messagebox


class Statistics(General):
    image = None

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)

        flag = True
        if self.title_name == "Moderators":
            flag = False
        Label(self.root, text="Statistics of " + self.uname, font=("Lucida Grande", 22, "bold"), bg="#2b509c",
              fg="#f64424").place(x=660, y=50, width=600, height=40)

        if flag:
            parts = fb.db.child("Users").child(self.uname).get()
        else:
            parts = fb.db.child("Moderators").child(self.uname).get()
        list_of_stat = []
        name_mail = []
        for p in parts:
            if type(p.val()) is not dict:
                name_mail.append(Label(self.root, text=p.key() + ': ' + p.val(), font=('Kotlin', 16, 'bold')))
                if p.key() == 'Mail':
                    email = p.val()
            else:
                if flag:
                    items = fb.db.child("Users").child(self.uname).child("Buys").get()
                    for i in items:
                        list_of_stat.append(
                            Label(self.root, text=i.key() + ': ' + i.val(), font=('Kotlin', 12, 'bold')))
                else:
                    items = fb.db.child("Moderators").child(self.uname).child("Work").get()
                    for i in items:
                        for j in i.val():
                            list_of_stat.append(
                                Label(self.root, text=j + ': ' + i.val()[j], font=('Kotlin', 12, 'bold')))

        pady = 120
        for lab in name_mail:
            lab.place(x=5, y=pady)
            pady += 40

        if flag:
            Label(self.root, text="Buys of " + self.uname + ':', font=('Kotlin', 16, 'bold')).place(x=5, y=pady)
        else:
            Label(self.root, text="Work of " + self.uname + ':', font=('Kotlin', 16, 'bold')).place(x=5, y=pady)

        pady += 40
        padx = 20
        for b in list_of_stat:
            if padx < 1920:
                if pady < 1040:
                    b.place(x=padx, y=pady)
                    pady += 30
                else:
                    pady = 200
                    padx += 750
                    b.place(x=padx, y=pady)
                    pady += 30

        delete = Button(root, text="Delete " + self.uname, font=("Lucida Grande", 11, 'bold'), bg="white", fg="#fc9d17",
                        borderwidth=5, command=lambda: self.delete_user(email, flag))
        delete.place(x=1660, width=190, height=40)
        if not flag:
            change = Button(root, text="Make User", font=("Lucida Grande", 11, 'bold'), bg="white", fg="#fc9d17",
                            borderwidth=5, command=lambda: self.change(flag))
            change.place(x=1440, width=190, height=40)
        else:
            change = Button(root, text="Make Moderator", font=("Lucida Grande", 11, 'bold'), bg="white", fg="#fc9d17",
                            borderwidth=5, command=lambda: self.change(flag))
            change.place(x=1440, width=190, height=40)

        back = Button(root, text="⮪", command=self.users, font=("Lucida Grande", 20),
                      fg='#f64424', bg='white', borderwidth=5)
        back.place(x=1, y=1, width=190, height=40)

    def delete_user(self, mail, ind):
        flag = True
        try:
            user = fa.auth.get_user_by_email(mail)
            uid = user.uid
            fa.auth.delete_user(uid)
            if ind:
                fb.db.child("Users").child(self.uname).remove()
            else:
                fb.db.child("Moderators").child(self.uname).remove()
        except Exception:
            flag = False
            messagebox.showerror("Error!", "Something went wrong!")

        if flag:
            messagebox.showinfo("Successful", "You have deleted " + self.uname)
            self.users()

    def change(self, ind):
        if ind:
            fb.db.child("Users").child(self.uname).child("Buys").remove()
            flag = True
            try:
                name = fb.db.child("Users").child(self.uname).get()
                fb.db.child("Moderators").child(self.uname).update(name.val())
                fb.db.child("Users").child(self.uname).remove()
            except Exception:
                flag = False
                messagebox.showerror("Error", "Something went wrong!")

            if flag:
                messagebox.showinfo("Successful", "You have added " + self.uname + " as Moderator")
        else:
            fb.db.child("Moderators").child(self.uname).child("Work").remove()
            flag = True
            try:
                name = fb.db.child("Moderators").child(self.uname).get()
                fb.db.child("Users").child(self.uname).update(name.val())
                fb.db.child("Moderators").child(self.uname).remove()
            except Exception:
                flag = False
                messagebox.showerror("Error", "Something went wrong!")

            if flag:
                messagebox.showinfo("Successful", "You have added " + self.uname + " as Moderator")
