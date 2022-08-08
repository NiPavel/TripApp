from tkinter import *
from tkinter import messagebox
from general import General
import firebase as fb
import urllib.parse
from PIL import Image, ImageTk
import io
import fa
from datetime import date


class Button_Hotels(General):
    image = None
    image1 = None
    image2 = None
    image3 = None

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)

        # Label(self.root, text=self.pname, font=('Cambria', 20, 'italic')).place(x=600, y=20)
        Label(self.root, text=self.pname, font=("Lucida Grande", 30, "bold"), bg="#2b509c", fg="#f64424") \
            .place(width=1800, height=60, x=60, y=60)

        if self.ind != "Description":
            descr = fb.db.child("Description").get()
            for n in descr:
                if self.pname == n.key():
                    self.description(pname)

            parts = fb.db.child("Counter").get()
            number_of_pics = 0
            for n in parts:
                if self.pname == n.key():
                    number_of_pics = n.val()

            for i in range(1, 5):
                data = None
                flag = True
                try:
                    path_on_fb = "images/{0}/{1}/".format(self.cname, self.pname) + str(i) + ".jpg"
                    url = fb.storage.child(path_on_fb).get_url(None)
                    data = urllib.request.urlopen(url).read()
                except Exception:
                    flag = False

                if flag:
                    im = Image.open(io.BytesIO(data))
                    resized_image = im.resize((300, 250), Image.ANTIALIAS)
                    if i == 1:
                        self.image = ImageTk.PhotoImage(resized_image, master=self.root)
                        label1 = Label(self.root, image=self.image)
                        label1.place(x=-100 + (300 * i), y=230)
                    elif i == 2:
                        self.image1 = ImageTk.PhotoImage(resized_image, master=self.root)
                        label1 = Label(self.root, image=self.image1)
                        label1.place(x=-100 + (300 * i), y=230)
                    elif i == 3:
                        self.image2 = ImageTk.PhotoImage(resized_image, master=self.root)
                        label1 = Label(self.root, image=self.image2)
                        label1.place(x=-100 + (300 * i), y=230)
                    else:
                        self.image3 = ImageTk.PhotoImage(resized_image, master=self.root)
                        label1 = Label(self.root, image=self.image3)
                        label1.place(x=-100 + (300 * i), y=230)

        parts = fb.db.child("Cities").child(self.cname).get()
        oname = None
        for n in parts:
            if self.pname in n.val():
                oname = n.key()

        if self.ind == 'del':
            delete = Button(self.root, text="Delete", font=("Lucida Grande", 11),
                          fg='#fc9d17', bg='white', borderwidth=5, command=self.do_delete)
            delete.place(x=1466, width=142, height=40)

            back = Button(root, text="⮪", command=self.go_to_cart, font=("Lucida Grande", 20),
                          fg='#f64424', bg='white', borderwidth=5)
            back.place(x=1, y=1, width=142, height=40)

            shop_cart = Button(self.root, text="🛒", font=('Lucida Grande', 12, 'bold'), bg="white", fg="#fc9d17",
                               borderwidth=5, command=self.go_to_cart)
            shop_cart.place(x=1638, width=40, height=40)

        elif self.ind == 'delete_part':
            # delete = Button(self.root, text="Delete", borderwidth=5, command=lambda: self.delete_part(oname), width=17)
            # delete.place(x=1320, y=770)
            # back = Button(self.root, text="<<", borderwidth=5, command=lambda: self.deletePart(oname), width=20)
            # back.grid(row=0, column=0, stick='we')
            delete = Button(self.root, text="Delete", font=("Lucida Grande", 11),
                            fg='#fc9d17', bg='white', borderwidth=5, command=lambda: self.delete_part(oname))
            delete.place(x=1466, width=142, height=40)

            back = Button(root, text="⮪", command=lambda: self.deletePart(oname), font=("Lucida Grande", 20),
                          fg='#f64424', bg='white', borderwidth=5)
            back.place(x=1, y=1, width=142, height=40)

        elif self.ind == 'Description':
            description_lab = Label(self.root, text="Enter a description about " + self.pname + " :",
                                    font=("Times New Roman", 18, 'bold'), bg='grey')
            description_lab.place(x=20, y=100)

            d_entry = Text(self.root, width=170, bd=5)
            d_entry.place(x=40, y=150, height=450)

            add = Button(self.root, text="Add", borderwidth=5, command=lambda: self.addDescr(d_entry.get("1.0", END)),
                         width=17)
            add.place(x=1320, y=770)

            back = Button(root, text="⮪", command=lambda: self.deletePart("Description"), font=("Lucida Grande", 20),
                          fg='#f64424', bg='white', borderwidth=5)
            back.place(x=1, y=1, width=142, height=40)

        elif self.ind == "Del_Description":
            # delete = Button(self.root, text="Delete", borderwidth=5, command=self.del_description,
            #                 width=17)
            # delete.place(x=1320, y=770)
            #
            # back = Button(self.root, text="<<", borderwidth=5, command=lambda: self.deletePart("Del_Description"),
            #               width=20)
            # back.grid(row=0, column=0, stick='we')

            delete = Button(self.root, text="Delete", font=("Lucida Grande", 11),
                            fg='#fc9d17', bg='white', borderwidth=5, command=self.del_description)
            delete.place(x=1466, width=142, height=40)

            back = Button(root, text="⮪", command=lambda: self.deletePart("Del_Description"), font=("Lucida Grande", 20),
                          fg='#f64424', bg='white', borderwidth=5)
            back.place(x=1, y=1, width=142, height=40)

        elif self.ind == "Del_Pictures":
            for i in range(1, 5):
                flag = True
                try:
                    path_on_fb = "images/{0}/{1}/".format(self.cname, self.pname) + str(i) + ".jpg"
                    url = fb.storage.child(path_on_fb).get_url(None)
                    data = urllib.request.urlopen(url).read()
                except Exception:
                    flag = False

                if flag:
                    # delete1 = Button(self.root, text="Delete " + str(i) + "-st Picture", borderwidth=5,
                    #                  command=lambda m=i: self.del_pics(m), width=17)
                    # delete1.place(x=0 + (i * 300), y=500)
                    delete = Button(self.root, text="Delete " + str(i) + " Picture", font=("Lucida Grande", 10),
                                    fg='#fc9d17', bg='white', borderwidth=5, command=lambda m=i: self.del_pics(m))
                    delete.place(x=1466, width=142, height=40)

            # back = Button(self.root, text="<<", borderwidth=5, command=lambda: self.deletePart("Del_Pictures"),
            #               width=20)
            # back.grid(row=0, column=0, stick='we')
            back = Button(root, text="⮪", command=lambda: self.deletePart("Del_Pictures"), font=("Lucida Grande", 20),
                          fg='#f64424', bg='white', borderwidth=5)
            back.place(x=1, y=1, width=142, height=40)

        else:
            buy = Button(self.root, text="Add to cart", font=("Lucida Grande", 11, 'bold'), bg="white", fg="#fc9d17",
                         borderwidth=5, command=self.do_buy)
            buy.place(x=1320, y=770, width=142, height=40)

            if General.title_name == 'Cities':
                back = Button(root, text="⮪", command=self.go_to_cities(), font=("Lucida Grande", 20),
                              fg='#f64424', bg='white', borderwidth=5)
                back.place(x=1, y=1, width=142, height=40)
            else:
                back = Button(root, text="⮪", command=self.go_to_parts, font=("Lucida Grande", 20),
                              fg='#f64424', bg='white', borderwidth=5)
                back.place(x=1, y=1, width=142, height=40)
            shop_cart = Button(self.root, text="🛒", font=('Lucida Grande', 12, 'bold'), bg="white", fg="#fc9d17",
                               borderwidth=5, command=self.go_to_cart)
            shop_cart.place(x=1638, width=40, height=40)

    def description(self, name):
        Label(self.root, text=fb.db.child("Description").child(name).get().val(), font=('Helvetica', 10, 'bold'), bd=1,
              relief='sunken').place(x=30, y=650)

    def do_buy(self):
        messagebox.showinfo("Thank you for your charge!", "You can see your item in your shopping cart.")
        # Label(self.root, text='Thank you for your charge!\n You can see your item in your shopping cart.',
        #       font=('Halvetica', 10, 'bold')).place(x=1150, y=720)
        self.list_p.append([self.pname, self.pprice])

    def go_to_cart(self):
        import cart
        General.ind = 'buy'
        master = Tk()
        master.geometry("800x640")
        master.title("Shopping Cart")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        cart.User(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, 'Else', self.ind)
        self.root.destroy()

    def do_delete(self):
        # del_text = Label(self.root, text="You've deleted a " + self.pname + "\nfrom your shopping cart!")
        # del_text.place(x=1150, y=720)
        messagebox.showinfo("Thank you for your change!", "You've deleted a " + self.pname + "\nfrom your shopping cart!")
        for i in self.list_p:
            if i[0] == self.pname:
                self.list_p.remove(i)

    def delete_part(self, name):
        flag = True
        try:
            fb.db.child("Cities").child(self.cname).child(name).child(self.pname).remove()
        except Exception:
            flag = False
            messagebox.showerror("Error!", "Something went wrong!")

        if flag:
            today = date.today()
            fb.db.child("Moderators").child(self.uname).child("Work").child("Delete Place").update(
                {self.pname: "Did delete at " + str(today)})
            messagebox.showinfo("Successful", "You have deleted a " + self.pname)

    def addDescr(self, text):
        flag = True
        try:
            fb.db.child("Description").update({self.pname: text})
        except Exception:
            flag = False
            messagebox.showerror("Error!", "Something went wrong!")

        if flag:
            today = date.today()
            fb.db.child("Moderators").child(self.uname).child("Work").child("Add Description").update(
                {self.pname: "Added a description at " + str(today)})
            messagebox.showinfo("Successful", "You have added a description for " + self.pname)

    def del_description(self):
        flag = True
        try:
            parts = fb.db.child("Description").get()
            for n in parts:
                if self.pname == n.key():
                    fb.db.child("Description").update({self.pname: None})
        except Exception:
            flag = False
            messagebox.showerror("Error!", "Something went wrong!")

        if flag:
            today = date.today()
            fb.db.child("Moderators").child(self.uname).child("Work").child("Delete Description").update(
                {self.pname: "Deleted description at " + str(today)})
            messagebox.showinfo("Successful", "You have deleted a description from " + self.pname)

    def del_pics(self, number):
        count = None
        parts = fb.db.child("Counter").get()
        for n in parts:
            if self.pname == n.key():
                count = n.val()
            else:
                count = 0

        flag = True
        try:
            path_on_fb = "images/{0}/{1}/".format(self.cname, self.pname) + str(number) + ".jpg"
            bucket = fa.admin_storage.bucket()
            blob = bucket.blob(path_on_fb)
            blob.delete()
        except Exception:
            flag = False
            messagebox.showerror("Error!", "Something went wrong!")

        if flag:
            today = date.today()
            fb.db.child("Moderators").child(self.uname).child("Work").child("Delete Picture").update(
                {self.pname: "Deleted a picture at " + str(today)})
            messagebox.showinfo("Successful", "You have deleted a " + str(number) + "picture from the " + self.pname)
            count -= 1
            fb.db.child("Counter").update({self.pname: count})
