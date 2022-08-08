from tkinter import *
from login import Login
from tkinter import messagebox
import firebase as fb
import menu
import cities
import login


class Moderator(Login):

    def __init__(self, root):
        super().__init__(root)
        Label(root, text="Moderator Log In", font=("Lucida Grande", 22, "bold"), fg='#f64424',
              bg='#2b509c').place(x=90, y=50, width=380, height=50)

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
            temp_list = fb.db.child("Moderators").get()
            for n in temp_list:
                if n.val().get("Mail") == m.get():
                    self.uname = n.val().get("Name")

            if self.uname is None:
                flag1 = False

            if flag1:
                temp_m = Tk()
                temp_m.after(1, lambda: temp_m.focus_force())
                temp_m.title("Moderator Interface")
                temp_m.geometry("560x440+680+213")
                temp_m.resizable(False, False)
                cities.Cities(temp_m, self.list_p, '', self.uname, m.get(), '', '', 'Cities', '')
                self.root.destroy()

            else:
                messagebox.showerror("Wrong Login!",
                                     "You have no permission to login with this email!\n"
                                     "Try to enter like a user.")
                self.login_press()

    def forgotPass(self):
        import password
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.geometry("560x440+680+213")
        temp_m.resizable(False, False)
        temp_m.title("Password Recovery")
        password.Forgot_Pass(temp_m, 'moderator')
        self.root.destroy()

    def login_press(self):
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title('Log In')
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        login.Login(master)
        self.root.destroy()
