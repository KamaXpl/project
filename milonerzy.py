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
root.configure(bg="black")

# wejscie do gry

bg = tkk.PhotoImage(file = "milionerzy1.png")

play_img = tkk.Label(image=bg)
play_img.place(x=0, y=0)

 # przycisk Zagraj 

play = tkk.PhotoImage(file="guzik-zagraj.png")

button = tkk.Button(root, image=play)
button.place(x=700, y=700)

# przycisk Info

info = tkk.PhotoImage(file="guzik-informacje.png")

button = tkk.Button(root, image=info)
button.place(x=1685, y=770)

root.mainloop()

