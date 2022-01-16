from tkinter import *
import firebase as fb
from general import General


class Description(General):

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind, name):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        self.name = name
        flag = True
        if self.name == "Del_Description" or self.name == "Del_Pictures":
            flag = False

        if flag:
            Label(self.root, text=name + " of the " + self.cname, font=("Cambria", 20, 'italic')).grid(row=1, column=3,
                                                                                                       pady=10)
        else:
            Label(self.root, text=name[4:] + " of the " + self.cname, font=("Cambria", 20, 'italic')).grid(row=1, column=3,
                                                                                                       pady=10)

        parts = fb.db.child('Cities').child(self.cname).get()
        column_count = 0
        for i in parts:
            part_list = []

            Label(root, text=i.key(), font=("Times New Roman", 18, "bold")).grid(row=2, column=column_count)
            temp_plist = fb.db.child('Cities').child(self.cname).child(i.key()).get()
            for p in temp_plist:
                c = p.key()
                t = p.val()
                if self.name == "Pictures":
                    part_list.append(Button(self.root, text=c + ':' + t, borderwidth=5,
                                            command=lambda m=c, y=t: self.goto_pic(m)))
                elif self.name == "Del_Pictures":
                    part_list.append(Button(self.root, text=c + ':' + t, borderwidth=5,
                                            command=lambda m=c, y=t: self.goto_charge(name, m)))
                else:
                    part_list.append(Button(self.root, text=c + ':' + t, borderwidth=5,
                                            command=lambda m=c, y=t: self.goto_charge(self.name, m)))

            grid_count = 0
            for g in part_list:
                g.grid(row=3 + grid_count, column=column_count, stick='we', padx=20)
                grid_count += 1

            column_count += 1

        back = Button(root, text="<<", borderwidth=5, command=self.go_to_parts)
        back.grid(row=0, column=0, stick='we')

    def goto_pic(self, name):
        import add_pictures
        General.pname = name
        master = Tk()
        master.title("Delete Part")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        add_pictures.Pictures(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                            self.title_name, 'delete_part')
        self.root.destroy()