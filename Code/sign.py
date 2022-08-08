# import the library of tkinter
from tkinter import *
from tkinter import messagebox
import firebase as fb
import menu
import cities


class Sign_up:
    root = None
    list_p = []
    uname = None

    def __init__(self, root):

        self.root = root
        # A Label widget to show in toplevel

        Label(self.root, bg='#2b509c').place(x=0, y=0, relwidth=1, relheight=1)

        Label(root, text="Registration", font=("Lucida Grande", 22, "bold"), fg='#f64424',
              bg='#2b509c').place(x=155, y=50, width=250, height=50)

        # a label for entering email
        Label(root, text="Enter email:", font=('Lucida Grande', 10, 'italic'), fg="#fc9d17",
              bg='#2b509c', anchor='w').place(x=45, y=158, width=150, height=50)
        # a label for entering password
        Label(root, text="Enter password:", font=('Lucida Grande', 10, 'italic'), fg="#fc9d17",
              bg='#2b509c', anchor='w').place(x=45, y=197, width=150, height=50)
        Label(root, text="Repeat password:", font=('Lucida Grande', 10, 'italic'), fg="#fc9d17",
              bg='#2b509c', anchor='w').place(x=45, y=236, width=150, height=50)
        Label(root, text="Enter your name:", font=('Lucida Grande', 10, 'italic'), fg="#fc9d17",
              bg='#2b509c', anchor='w').place(x=45, y=275, width=150, height=50)

        # creating field for entering email
        mail = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        mail.place(x=215, y=160, width=300, height=40)
        mail.focus()
        # creating field for entering password
        password = Entry(root, show='*', width=50, fg="blue", justify=CENTER, bd=3)
        password.place(x=215, y=200, width=300, height=40)

        show_pass = Button(root, text="🗝", font=("Lucida Grande", 13, "bold"), fg='#fc9d17', bg='white', borderwidth=5,
                           command=lambda: self.show(password))
        show_pass.place(x=521, y=200, width=35, height=40)

        password2 = Entry(root, show='*', width=50, fg="blue", justify=CENTER, bd=3)
        password2.place(x=215, y=240, width=300, height=40)
        # creating a name
        name = Entry(root, width=50, fg='blue', justify=CENTER, bd=3)
        name.place(x=215, y=280, width=300, height=40)
        # creating button for confirmation of data

        ok = Button(root, text="Sign Up", font=("Lucida Grande", 15, "bold"), fg='#f64424', borderwidth=5,
                    command=lambda: self.registration(mail, password, password2, name))
        ok.place(x=405, y=340, width=110, height=50)

        # creating button for back to previous page
        back = Button(root, text="⮪", command=self.go_to_menu, font=("Lucida Grande", 20),
                      fg='#f64424', borderwidth=5)
        back.place(x=1, y=1, width=80, height=40)

    def go_to_menu(self):
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.title('TriPerAdvise')
        temp_m.geometry("560x440+680+213")
        temp_m.resizable(False, False)
        menu.Menu(temp_m)
        self.root.destroy()

    def registration(self, m, p, p2, name):
        flag = False
        if p.get() != p2.get():
            messagebox.showwarning("Wrong password!", "The passwords aren't the same!")
            p.delete(0, END)
            p2.delete(0, END)
            p.focus()
            return
        if len(name.get()) == 0:
            messagebox.showwarning("Wrong name!", "Enter a name please!")
            name.focus()
            return
        try:
            fb.auth.create_user_with_email_and_password(m.get(), p.get())
            flag = True
        except Exception:
            messagebox.showwarning("Wrong mail or password!", "The password should to be more than 6 characters\n"
                                                              "or the mail is incorrect\nor the mail has been already registred!")
            m.delete(0, END)
            p.delete(0, END)
            p2.delete(0, END)
            name.delete(0, END)
            m.focus()
        if flag:
            fb.db.child("Users").child(name.get()).update({"Mail": m.get(), "Name": name.get()})
            temp_m = Tk()
            temp_m.after(1, lambda: temp_m.focus_force())
            temp_m.title("Cities")
            temp_m.geometry("560x440+680+213")
            temp_m.resizable(False, False)
            temp_list = fb.db.child("Users").get()
            for n in temp_list:
                if n.val().get("Mail") == m.get():
                    self.uname = n.val().get("Name")
            cities.Cities(temp_m, self.list_p, '', self.uname, m.get(), '', '', 'Cities', '')
            self.root.destroy()

    def show(self, password):
        if password.cget('show') == '':
            password.config(show='*')
        else:
            password.config(show='')
