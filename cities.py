from tkinter import *
import firebase as fb
from general import General


class Cities(General):
    image = None

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        self.mini_screen_bg()
        Label(self.root, text="CITIES", font=("Lucida Grande", 30, "bold"), bg="#2b509c", fg="#f64424") \
            .place(y=50, width=560, height=60)
        Button(root, text="Log Out", font=("Lucida Grande", 11, 'bold'), bg="white", fg="#fc9d17",
               borderwidth=5, command=self.log_out).place(x=470, width=90, height=40)

        flag = False
        moders = fb.db.child('Moderators').get()
        if moders.val():
            for n in moders:
                if n.val().get("Mail") == self.mail:
                    flag = True

        cities = fb.db.child("Cities").get()
        listOfCities = []
        for i in cities:
            c = i.key()
            listOfCities.append(
                Button(self.root, text=c, font=('Lucida Grande', 14, 'bold'), bg="white", fg="#fc9d17", borderwidth=5,
                       command=lambda m=c: self.go_to_parts1(m), width=20))

        padx = 8
        pady = 150
        for i in listOfCities:
            if padx < 560:
                if pady < 440:
                    i.place(x=padx, y=pady, width=140, height=50)
                    pady += 58
                else:
                    pady = 150
                    padx += 202
                    i.place(x=padx, y=pady, width=140, height=50)
                    pady += 58

        if not flag:
            shop_cart = Button(self.root, text="🛒", font=('Lucida Grande', 12, 'bold'), bg="white", fg="#fc9d17",
                               borderwidth=5, command=self.go_to_cart)
            shop_cart.place(x=1690, width=40, height=40)

    def go_to_cart(self):
        import cart
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.resizable(False, False)
        master.title("Shopping Cart")
        master.attributes('-fullscreen', True)
        cart.User(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, "Cities",
                  self.ind)
        self.root.destroy()

