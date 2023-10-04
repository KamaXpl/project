import random
import tkinter as tkk
from tkinter import *
import mysql.connector


import MySQLdb

milionerzy = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="milionerzy")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = milionerzy.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM pyt ")
cur.execute("SELECT * FROM odp ")

# print all the first cell of all the rows
for row in cur.fetchall():
    print ("Poprawna odp: ", row[5])



root = tkk.Tk()
root.geometry('1920x1080')
root.resizable(False, False)
root.configure(bg="black")



Image = tkk.PhotoImage(file = "milionerzy.png")
play_img = tkk.Label(width=600, image=Image)
play_btn = tkk.Button(root, width=20, height=10, text="Zagraj", font="Arial", fg="White", bg="black")
play_btn.place(x=860, y=800)
play_img.place(x=660, y=100)




root.mainloop()

