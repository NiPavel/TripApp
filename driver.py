import menu
from tkinter import *
# import firebase as fb
# import urllib.parse
# from PIL import Image, ImageTk
# import io

root = Tk()
root.after(1, lambda: root.focus_force())
root.title('TriPerAdvise')
root.geometry("560x440+680+213")
root.resizable(False, False)
menu.Menu(root)

root.mainloop()
