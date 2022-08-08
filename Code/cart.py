from tkinter import *
from tkinter import messagebox
from general import General
import smtplib
from email.message import EmailMessage
import firebase as fb

class User(General):
    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)

        # cart = Label(root, text='Shopping cart', font=('Times New Roman', 21, 'bold'))
        # cart.place(x=550, y=20)
        Label(self.root, text=self.cname, bg="#2b509c", fg="#2b509c", font=("Lucida Grande", 25, "bold")) \
            .grid(row=1, column=2, pady=35)  # none
        Label(self.root, text='Shopping cart', font=("Lucida Grande", 30, "bold"), bg="#2b509c", fg="#f64424") \
            .place(width=800, height=60, x=560, y=30)

        # hello = Label(root, text='Hello ' + self.uname + '!', font=('Times New Roman', 18, 'bold'))
        # hello.place(x=600, y=70)
        Label(self.root, text=self.cname, bg="#2b509c", fg="#2b509c", font=("Lucida Grande", 25, "bold")) \
            .grid(row=1, column=2, pady=70)  # none
        Label(self.root, text='Hello ' + self.uname + '!', font=("Lucida Grande", 24, "bold"), bg="#2b509c", fg="#fc9d17") \
            .place(width=800, height=50, x=560, y=100)

        Label(root, text='Your charges', font=('Times New Roman', 16, 'bold'), bg="white", fg="#f64424")\
            .grid(row=2, column=0, stick='we', pady=20, padx=20)
        Label(root, text='Price', font=('Times New Roman', 16, 'bold'), bg="white", fg="#f64424")\
            .grid(row=2, column=1, stick='we', pady=20, padx=20)
        Label(root, text='Price of the trip', font=('Times New Roman', 16, 'bold'), bg="white", fg="#f64424")\
            .grid(row=2, column=2, stick='we')
        count = 0
        price = 0
        if list_p is not None and len(self.list_p) != 0:
            for i in self.list_p:
                if len(i) != 0:
                    hotel = Button(root, text=i[0], font=('Times New Roman', 14, 'bold'), borderwidth=5, bg="white",
                                   fg="black", command=lambda m=i[0]: self.goto_charge('del', m))
                    hotel.grid(row=3 + count, column=0, stick='we')
                    price += int(i[1][1:])
                    p = Label(self.root, text=i[1], font=('Times New Roman', 14, 'bold'), bg="white", fg="black")
                    p.grid(row=3 + count, column=1)
                    count += 1

        sum_of_prices = Label(self.root, text='₪' + str(price), font=('Times New Roman', 14, 'bold'), bg="white", fg="#f64424")
        sum_of_prices.grid(row=3, column=2)

        # refresh = Button(root, text="🔄", font=('Lucida Grande', 14, 'bold'), bg="white", fg="red", borderwidth=5,
        #               command=self.refresh)
        # refresh.place(x=1294, width=40, height=40)

        change_name = Button(self.root, text='Change Name', font=("Lucida Grande", 11, 'bold'),
                             bg="white", fg="#fc9d17", borderwidth=5, command=self.changeName)
        change_name.place(x=1536, width=142, height=40)

        buy = Button(self.root, text="Checkout!", font=("Lucida Grande", 11, 'bold'),
                             bg="white", fg="#fc9d17", borderwidth=5, command=lambda: self.do_buy(price))
        buy.place(x=1364, width=142, height=40)

        # back = Button(root, text="<<", borderwidth=5, command=self.go_back, width=20)
        # back.grid(row=0, column=0)
        back = Button(root, text="⮪", command=self.go_back, font=("Lucida Grande", 20),
                      fg='#f64424', bg='white', borderwidth=5)
        back.place(x=1, y=1, width=142, height=40)


    def go_back(self):
        import cities
        import parts
        import parts_after_button
        master = Tk()
        master.after(1, lambda: master.focus_force())
        master.attributes('-fullscreen', True)
        if self.title_name == 'Cities':
            master.title(self.title_name)
            cities.Cities(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                          self.title_name, self.ind)
            self.root.destroy()
        elif self.title_name == 'Parts':
            master.title('Our menu')
            parts.Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                         self.title_name, self.ind)
            self.root.destroy()
        else:
            master.title(self.title_name)
            parts_after_button.Button_Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname,
                                             self.pprice, self.title_name, self.ind)
            self.root.destroy()

    def do_buy(self, price):
        if len(self.list_p) > 0:
            Label(self.root,
                  text="Thank you for your charge!\n The mail with details of your charge has sent to your mail.").place(
                x=1150, y=720)
            file = open("mail_for_buy.txt", 'w+')
            file.write('Hi ' + self.uname + '!\n'
                                            ' We’re so excited that you’ve decided to purchase in our application.\n'
                                            ' It’s designed to help you to choose the best trip in Israel.\n'
                                            ' You can expect to hear from us many times a month with special offers, product updates, and more.\n'
                                            ' Contact us at TriPerAdvise@gmail.com if you have any questions.\n'
                                            'Your list of purchases:\n')
            for item in self.list_p:
                file.writelines(item[0] + ' \n')
            file.close()

            file = open('mail_for_buy.txt', 'a')
            file.write("The price of the trip is: " + str(price) + " New Shekel.\n")
            file.close()

            file = open('mail_for_buy.txt', 'r+')
            msg = EmailMessage()
            msg.set_content(file.read())

            msg['Subject'] = f'Thank you for your purchasing on T1riPerAdvise'
            msg['From'] = 'TriPerAdvise@gmail.com'
            msg['To'] = self.mail

            # Send the message via our own SMTP server.
            s = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
            s.login('pavelni@ac.sce.ac.il', '3bw1NpMtdAsTf0Jn')
            s.send_message(msg)
            s.quit()

            for part in self.list_p:
                fb.db.child("Users").child(self.uname).child("Buys").update({part[0]: part[1]})
        else:
            messagebox.showerror("Your list of buys is empty!", "Please choose one trip at least!")

    def changeName(self):
        import name_change
        temp_m = Tk()
        temp_m.after(1, lambda: temp_m.focus_force())
        temp_m.geometry("560x440+680+213")
        temp_m.title("Change Name")
        temp_m.resizable(False, False)
        name_change.Change(temp_m, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                           self.title_name, self.ind)
        self.root.destroy()
