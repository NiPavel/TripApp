from tkinter import *
import firebase as fb
from general import General


class Hotels(General):
    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        # Label(self.root, text=self.cname, font=('Cambria', 20, 'italic')).grid(row=1, column=3, pady=20)
        # Label(self.root, text=self.cname, font=("Lucida Grande", 30, "bold"), bg="#2b509c", fg="#f64424") \
        #     .grid(row=1, column=3, pady=20)

        Label(self.root, text=self.cname, bg="#2b509c", fg="#2b509c", font=("Lucida Grande", 25, "bold")) \
            .grid(row=1, column=2, pady=35)  # none
        Label(self.root, text=self.cname, font=("Lucida Grande", 30, "bold"), bg="#2b509c", fg="#f64424") \
            .place(width=800, height=60, x=560, y=60)

        flag = False
        moders = fb.db.child('Moderators').get()
        if moders.val():
            for n in moders:
                if n.val().get("Mail") == self.mail:
                    flag = True

        parts = fb.db.child('Cities').child(self.cname).get()
        column_count = 0
        for i in parts:
            part_list = []
            part_list_del = []
            if not flag:
                # Label(root, text=i.key(), font=("Times New Roman", 18, "bold")).grid(row=2, column=column_count, pady=10)
                Label(self.root, text=i.key(), font=('Lucida Grande', 18, 'bold'), bg="white", fg="#fc9d17") \
                    .grid(row=2, column=column_count, pady=10)
                temp_plist = fb.db.child('Cities').child(self.cname).child(i.key()).get()
                for p in temp_plist:
                    c = p.key()
                    t = p.val()
                    part_list.append(Button(self.root, text=c + ': ' + t, borderwidth=5, bg="white", fg="black",
                                            command=lambda m=c, y=t: self.chosed_hotel(m, y)))

            else:
                part_list.append(Button(self.root, text='Add ' + i.key(), borderwidth=5, width=15, height=5,
                                        bg="white", command=lambda m=i.key(): self.addPart(m)))
                part_list_del.append(Button(self.root, text='Delete ' + i.key(), borderwidth=5, width=15, height=5,
                                            bg="white", command=lambda m=i.key(): self.deletePart(m)))
            grid_count = 0
            for g in part_list:
                g.grid(row=3 + grid_count, column=column_count, stick='we', padx=17)
                grid_count += 1

            for g in part_list_del:
                g.grid(row=4 + grid_count, column=column_count, stick='we', padx=20, pady=20)
                grid_count += 1
            column_count += 1

        if flag:
            add_description = Button(self.root, text="Add Description", borderwidth=5, width=15, height=5,
                                     bg="white", command=lambda: self.deletePart('Description'))
            add_description.grid(row=3, column=column_count, stick='we', padx=20)

            del_description = Button(self.root, text="Delete Description", borderwidth=5, width=15, height=5,
                                     bg="white", command=lambda: self.deletePart('Del_Description'))
            del_description.grid(row=5, column=column_count, stick='we', padx=20)
            column_count += 1

            add_pictures = Button(self.root, text="Add Pictures", borderwidth=5, width=15, height=5,
                                  bg="white", command=lambda: self.deletePart('Pictures'))
            add_pictures.grid(row=3, column=column_count, stick='we', padx=20)

            del_pictures = Button(self.root, text="Delete Pictures", borderwidth=5, width=15, height=5,
                                  bg="white", command=lambda: self.deletePart('Del_Pictures'))
            del_pictures.grid(row=5, column=column_count, stick='we', padx=20)

        # back = Button(root, text="<<", borderwidth=5, command=self.go_to_cities)
        # back.grid(row=0, column=0, stick='we')
        back = Button(root, text="⮪", command=self.go_to_cities, font=("Lucida Grande", 20),
                      fg='#f64424', bg='white', borderwidth=5)
        back.place(x=1, y=1, width=142, height=40)

        if not flag:
            shop_cart = Button(self.root, text="🛒", font=('Lucida Grande', 12, 'bold'), bg="white", fg="#fc9d17",
                               borderwidth=5, command=self.go_to_cart)
            shop_cart.place(x=1638, width=40, height=40)

    def go_to_cart(self):
        import cart
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.resizable(False, False)
        master.title("Shopping Cart")
        master.attributes('-fullscreen', True)
        cart.User(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, "Parts",
                  self.ind)
        self.root.destroy()

    def addPart(self, name):
        import add_parts
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.resizable(False, False)
        master.title("Shopping Cart")
        master.attributes('-fullscreen', True)
        add_parts.addPart(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                          self.title_name, self.ind, name)
        self.root.destroy()
