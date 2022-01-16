from tkinter import *
import sys
import firebase as fb
import urllib.parse
from PIL import Image, ImageTk
import io


class General:
    cname = None
    pname = None
    pprice = None
    ind = None
    title_name = None
    image = None

    def __init__(self, root, list_p, cname='', uname='', mail='', pname='', pprice='', title_name='', ind=''):
        self.root = root
        self.list_p = list_p
        self.uname = uname
        self.mail = mail
        self.title_name = title_name
        self.full_screen_bg()
        self.root.after(1, lambda: self.root.focus_force())

        log_out = Button(root, text="Log Out", font=("Lucida Grande", 11, 'bold'), bg="white", fg="#fc9d17",
                         borderwidth=5, command=self.log_out)
        log_out.place(x=1708, width=142, height=40)

        exit = Button(root, text="❌", font=('Lucida Grande', 13, 'bold'), bg="white", fg="red", borderwidth=5,
                      command=self.exit_program)
        exit.place(x=1880, width=40, height=40)

    def full_screen_bg(self):
        path = "window/interface_bg.png"
        url = fb.storage.child(path).get_url(None)
        data = urllib.request.urlopen(url).read()
        im = Image.open(io.BytesIO(data))
        self.image = ImageTk.PhotoImage(im, master=self.root)
        Label(self.root, image=self.image).place(x=0, y=0, relwidth=1, relheight=1)

    def mini_screen_bg(self):
        path = "window/beach_edited.png"
        url = fb.storage.child(path).get_url(None)
        data = urllib.request.urlopen(url).read()
        im = Image.open(io.BytesIO(data))
        self.image = ImageTk.PhotoImage(im, master=self.root)
        Label(self.root, image=self.image).place(x=0, y=0, relwidth=1, relheight=1)

    def go_to_cities(self):
        import cities
        General.title_name = "Cities"
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.title("Cities")
        temp_m.geometry("560x440+680+213")
        temp_m.resizable(False, False)
        cities.Cities(temp_m, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, self.title_name,
                      self.ind)
        self.root.destroy()

    def go_to_parts(self):
        import parts
        General.title_name = 'Parts'
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title("Our menu")
        master.attributes('-fullscreen', True)
        parts.Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, self.title_name,
                     self.ind)
        self.root.destroy()

    def go_to_parts1(self, name):
        import parts
        General.title_name = 'Parts'
        General.cname = name
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title("Our menu")
        master.attributes('-fullscreen', True)
        parts.Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, self.title_name,
                     self.ind)
        self.root.destroy()

    def chosed_hotel(self, name, price):
        import parts_after_button
        General.title_name = 'Else'
        General.pname = name
        General.pprice = price
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title(name)
        master.attributes('-fullscreen', True)
        parts_after_button.Button_Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname,
                                         self.pprice, self.title_name, self.ind)
        self.root.destroy()

    def goto_charge(self, ind, name):
        import parts_after_button
        General.title_name = 'Else'
        General.ind = ind
        General.pname = name
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title(name)
        master.attributes('-fullscreen', True)
        parts_after_button.Button_Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname,
                                         self.pprice, self.title_name, self.ind)
        self.root.destroy()

    def deletePart(self, name):
        import delete_part
        import add_description
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.title("Delete Part")
        master.attributes('-fullscreen', True)
        if name == "Description" or name == "Del_Description" or name == 'Pictures' or name == 'Del_Pictures':
            add_description.Description(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                                        self.title_name, self.ind, name)
        else:
            General.ind = 'delete_part'
            delete_part.deletePart(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                                   self.title_name, self.ind, name)
        self.root.destroy()

    def go_to_admin_menu(self):
        import admin_menu
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.title("Admin Interface")
        temp_m.geometry("560x440+680+213")
        temp_m.resizable(False, False)
        admin_menu.Admin_Menu(temp_m, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                              self.title_name, self.ind)
        self.root.destroy()

    def users(self):
        import users
        master = Tk()
        master.after(1, lambda: master.focus_force())
        if self.title_name != "Moderators":
            master.title("Users")
        else:
            master.title("Moderators")
        master.geometry("560x440+680+213")
        master.resizable(False, False)
        users.Users(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                    self.title_name, self.ind)
        self.root.destroy()

    def goto_stat(self, name):
        import stat_of_user
        self.uname = name
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.resizable(False, False)
        temp_m.title("Statistics")
        temp_m.attributes('-fullscreen', True)
        stat_of_user.Statistics(temp_m, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                                self.title_name, self.ind)
        self.root.destroy()

    def log_out(self):
        import menu
        self.list_p = None
        self.cname = None
        self.uname = None
        self.mail = None
        self.pname = None
        self.pprice = None
        self.title_name = None
        self.ind = None
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.title('TriPerAdvise')
        temp_m.geometry("560x440+680+213")
        temp_m.resizable(False, False)
        menu.Menu(temp_m)
        self.root.destroy()

    def exit_program(self):
        raise SystemExit
        sys.exit()
