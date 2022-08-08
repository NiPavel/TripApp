from tkinter import *
from tkinter import messagebox
import login
import fa
import smtplib
from email.message import EmailMessage
import firebase as fb


class Forgot_Pass:

    def __init__(self, root, ind):
        self.root = root
        self.ind = ind

        Label(self.root, bg='#2b509c').place(x=0, y=0, relwidth=1, relheight=1)

        Label(root, text="Password Recovery", font=("Lucida Grande", 22, "bold"), fg='#f64424',
              bg='#2b509c').place(x=90, y=60, width=380, height=50)
        Label(root, text="Enter email:", font=('Lucida Grande', 10, 'italic'), fg="#fc9d17",
              bg='#2b509c', anchor='w').place(x=45, y=158, width=150, height=50)
        mail = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        mail.place(x=215, y=160, width=300, height=40)
        mail.focus()
        ok = Button(root, text="Send", font=("Lucida Grande", 15, "bold"), fg='#f64424', borderwidth=5,
                    command=lambda: self.enter(mail))
        ok.place(x=405, y=220, width=110, height=50)

        if self.ind == 'user':
            back = Button(root, text="⮪", command=self.go_to_login, font=("Lucida Grande", 20),
                          fg='#f64424', borderwidth=5)
            back.place(x=1, y=1, width=80, height=40)
        elif self.ind == 'moderator':
            back = Button(root, text="⮪", command=self.go_to_mod_login, font=("Lucida Grande", 20),
                          fg='#f64424', borderwidth=5)
            back.place(x=1, y=1, width=80, height=40)
        else:
            back = Button(root, text="⮪", command=self.go_to_admin_login, font=("Lucida Grande", 20),
                          fg='#f64424', borderwidth=5)
            back.place(x=1, y=1, width=80, height=40)

    def go_to_login(self):
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        master.title("Log In")
        login.Login(master)
        self.root.destroy()

    def go_to_mod_login(self):
        import mod_enter
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        master.title("Moderator Log In")
        mod_enter.Moderator(master)
        self.root.destroy()

    def go_to_admin_login(self):
        import admin_enter
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        master.title("Administrator Log In")
        admin_enter.Administrator(master)
        self.root.destroy()

    def enter(self, mail):
        flag = True
        try:
            user = fa.auth.get_user_by_email(mail.get())
        except Exception:
            messagebox.showerror("Wrong Email", "Enter correct e-mail!")
            flag = False
            mail.delete(0, END)
        if flag:
            link = fa.auth.generate_password_reset_link(mail.get())
            file = open("confirm_email.txt", "w+")
            file.write('Hello,\n'
                       'We received your request for reset the password in our application.\n'
                       'If it was you, please go to this link --> ' + link + '\n'
                       'If it was not you, just ignore this e-mail.\n'
                       'We are glad that you are with us.')
            file.close()

            file = open("confirm_email.txt", "r+")
            msg = EmailMessage()
            msg.set_content(file.read())

            msg['Subject'] = f'Reset password in TriPerAdvise'
            msg['From'] = 'TriPerAdvise@gmail.com'
            msg['To'] = mail.get()

            # Send the message via our own SMTP server.
            s = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
            s.login('pavelni@ac.sce.ac.il', '3bw1NpMtdAsTf0Jn')
            s.send_message(msg)
            s.quit()
            messagebox.showinfo("Reset password", "The mail with link to reset a password has sent!")
            temp_list = fb.db.child("Users").get()
            for n in temp_list:
                if n.val().get("Mail") == mail.get():
                    self.go_to_login()
                    return
            temp_list = fb.db.child("Moderators").get()
            for n in temp_list:
                if n.val().get("Mail") == mail.get():
                    self.go_to_mod_login()
                    return
            temp_list = fb.db.child("Administrators").get()
            for n in temp_list:
                if n.val().get("Mail") == mail.get():
                    self.go_to_admin_login()
                    return
