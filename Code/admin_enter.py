from tkinter import *
from login import Login
from tkinter import messagebox
import admin_menu
import firebase as fb
import menu
import login


class Administrator(Login):

    def __init__(self, root):
        super().__init__(root)
        Label(root, text="Administrator Log In", font=("Lucida Grande", 22, "bold"), fg='#f64424',
              bg='#2b509c').place(x=80, y=50, width=400, height=50)

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
            temp_list = fb.db.child("Administrators").get()
            for n in temp_list:
                if n.val().get("Mail") == m.get():
                    self.uname = n.val().get("Name")

            if self.uname is None:
                flag1 = False

            if flag1:
                temp_m = Tk()
                temp_m.title("Admin Interface")
                temp_m.geometry("560x440+680+213")
                temp_m.resizable(False, False)
                admin_menu.Admin_Menu(temp_m, self.list_p, '', self.uname, m.get(), '', '', 'Cities', '')
                self.root.destroy()

            else:
                messagebox.showerror("Wrong Login!",
                                     "You have no permission to login with this email!\n"
                                     "Try to enter like moderator or user.")
                self.go_to_menu()

    def forgotPass(self):
        import password
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.geometry("560x440+680+213")
        temp_m.resizable(False, False)
        temp_m.title("Password Recovery")
        password.Forgot_Pass(temp_m, 'admin')
        self.root.destroy()
