# import the library of tkinter
from tkinter import *
import sign
import login
import mod_enter
import admin_enter
import firebase as fb
import urllib.parse
from PIL import Image, ImageTk
import io


class Menu:
    image = None

    def __init__(self, root):
        self.root = root

        path = "window/beach_edited.png"
        url = fb.storage.child(path).get_url(None)
        data = urllib.request.urlopen(url).read()
        im = Image.open(io.BytesIO(data))
        self.image = ImageTk.PhotoImage(im, master=self.root)

        Label(self.root, image=self.image).place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.root, text="Welcome to TriPerAdvise!", bg="#2b509c", fg="#f64424",
              font=("Lucida Grande", 22, "bold")).place(x=30, y=12, width=500, height=50)
        Label(self.root, text="Plan your trip with us :)", bg="#2b509c", fg="#fc9d17",
              font=("Lucida Grande", 15, "bold")).place(x=130, y=70, width=300, height=40)

        sign_up = Button(root, text="Sign up", command=self.signup_press, font=("Lucida Grande", 15, "bold"),
                         bg="white", fg="#2b509c", borderwidth=5)
        sign_up.place(x=65, y=280, width=110, height=50)

        log_in = Button(root, text="Log in", command=self.login_press, font=("Lucida Grande", 15, "bold"),
                        borderwidth=5,
                        bg="white", fg="#2b509c")
        log_in.place(x=385, y=280, width=110, height=50)

        log_in_mod = Button(root, text="Moderator Login", command=self.login_mod_press, font=("Lucida Grande", 10),
                            borderwidth=4, fg="#f64424")
        log_in_mod.place(x=100, y=395, width=180, height=35)

        log_in_admin = Button(root, text="Administrator Login", command=self.login_admin_press,
                              font=("Lucida Grande", 10), borderwidth=4, fg="#f64424")
        log_in_admin.place(x=280, y=395, width=180, height=35)

    def signup_press(self):
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title('Sign Up')
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        sign.Sign_up(master)
        self.root.destroy()

    def login_press(self):
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title('Log In')
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        login.Login(master)
        self.root.destroy()



    def login_mod_press(self):
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title('Moderator Log In')
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        mod_enter.Moderator(master)
        self.root.destroy()



    def login_admin_press(self):
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title('Administrator Log In')
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        admin_enter.Administrator(master)
        self.root.destroy()
