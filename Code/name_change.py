from general import General
from tkinter import *
from tkinter import messagebox
import firebase as fb


class Change(General):

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)

        Label(self.root, bg='#2b509c').place(x=0, y=0, relwidth=1, relheight=1)
        Label(root, text="Change Name", font=("Lucida Grande", 22, "bold"), fg='#f64424',
              bg='#2b509c').place(x=140, y=50, width=280, height=50)
        Label(root, text="Enter new name:", font=('Lucida Grande', 10, 'italic'), fg="#fc9d17",
              bg='#2b509c', anchor='w').place(x=45, y=158, width=150, height=50)

        name = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        name.place(x=215, y=160, width=300, height=40)
        name.focus()

        change = Button(root, text="Change", font=("Lucida Grande", 15, "bold"), fg='#f64424', borderwidth=5,
                        command=lambda: self.do_change(name))
        change.place(x=405, y=260, width=110, height=50)

        back = Button(root, text="⮪", command=self.go_to_cart, font=("Lucida Grande", 20),
                      fg='#f64424', borderwidth=5)
        back.place(x=1, y=1, width=80, height=40)

    def do_change(self, name):
        try:
            temp_list = fb.db.child("Users").get()
            temp_data = fb.db.child("Users").child(self.uname).get()
            temp_mail = temp_data.val()["Mail"]
            temp_name = temp_data.val()["Name"]
            fb.db.child("Users").child(self.uname).remove()
            fb.db.child('Users').child(name.get()).update({"Mail": temp_mail, "Name": name.get()})
            self.uname = name.get()
            messagebox.showinfo("Successful", "You have changed your name!")
            # self.root.destroy()
            self.go_to_cart()
        except Exception:
            messagebox.showerror("Error!", "Something went wrong!")
            name.delete()
            name.focus()

    def go_to_cart(self):
        import cart
        master = Tk()
        master.title("Shopping Cart")
        master.attributes('-fullscreen', True)
        cart.User(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, self.title_name,
                  self.ind)
        self.root.destroy()
