from tkinter import *
from tkinter import messagebox
import firebase as fb
import menu
import cities
import password
import cart


class Login:
    list_p = []
    uname = None

    def __init__(self, root):
        self.root = root

        # A Label widget to show in toplevel
        Label(self.root, bg='#2b509c').place(x=0, y=0, relwidth=1, relheight=1)

        Label(root, text="Log In", font=("Lucida Grande", 22, "bold"), fg='#f64424',
              bg='#2b509c').place(x=155, y=50, width=250, height=50)
        Label(root, text="Enter email:", font=('Lucida Grande', 10, 'italic'), fg="#fc9d17",
              bg='#2b509c', anchor='w').place(x=45, y=158, width=150, height=50)
        Label(root, text="Enter password:", font=('Lucida Grande', 10, 'italic'), fg="#fc9d17",
              bg='#2b509c', anchor='w').place(x=45, y=197, width=150, height=50)

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

        # creating button for confirmation of data
        ok = Button(root, text="Log In", font=("Lucida Grande", 15, "bold"), fg='#f64424', borderwidth=5,
                    command=lambda: self.enter(mail, password))
        ok.place(x=405, y=260, width=110, height=50)
        # creating button for come back

        forgot_pass = Button(root, text="Forgot my password", font=("Lucida Grande", 10, "bold"), borderwidth=5,
                             fg="#fc9d17", command=self.forgotPass)
        forgot_pass.place(x=51, y=260, width=192, height=50)

        back = Button(root, text="⮪", command=self.go_to_menu, font=("Lucida Grande", 20),
                      fg='#f64424', bg='white', borderwidth=5)
        back.place(x=1, y=1, width=80, height=40)

    def go_to_menu(self):
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.title('TriPerAdvise')
        temp_m.geometry("560x440+680+213")
        temp_m.resizable(False, False)
        menu.Menu(temp_m)
        self.root.destroy()

    def enter(self, m, p):
        flag = False
        try:
            fb.auth.sign_in_with_email_and_password(m.get(), p.get())
            flag = True
        except Exception:
            messagebox.showwarning("Wrong mail or password!", "The mail or password is incorrect!")
            m.delete(0, END)
            p.delete(0, END)
            m.focus()
            return

        if flag:
            flag1 = True
            temp_list = fb.db.child("Users").get()
            for n in temp_list:
                if n.val().get("Mail") == m.get():
                    self.uname = n.val().get("Name")

            if self.uname is None:
                flag1 = False

            if flag1:
                # temp_m = Tk()
                # temp_m.resizable(False, False)
                # temp_m.title("Cities")
                # temp_m.attributes('-fullscreen', True)
                # cities.Cities(temp_m, self.list_p, '', self.uname, m.get(), '', '', 'Cities', '')
                # self.root.destroy()

                temp_m = Tk()
                temp_m.after(1, lambda: temp_m.focus_force())
                temp_m.title("Cities")
                temp_m.geometry("560x440+680+213")
                temp_m.resizable(False, False)
                cities.Cities(temp_m, self.list_p, '', self.uname, m.get(), '', '', 'Cities', '')
                self.root.destroy()

            else:
                messagebox.showerror("Wrong Login!",
                                     "You have no permission to login with this email!\n"
                                     "Try to enter like moderator or admin.")
                self.go_to_menu()

    def forgotPass(self):
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.title("Password Recovery")
        temp_m.geometry("560x440+680+213")
        temp_m.resizable(False, False)
        password.Forgot_Pass(temp_m, 'user')
        self.root.destroy()

    def show(self, password):
        if password.cget('show') == '':
            password.config(show='*')
        else:
            password.config(show='')
