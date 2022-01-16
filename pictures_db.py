import firebase as fb
import os
import general


def add_all_pictiures(pname):
    count = None
    parts = fb.db.child("Counter").get()
    for n in parts:
        if pname == n.key():
            count = n.val()
        else:
            count = 0

    # path =