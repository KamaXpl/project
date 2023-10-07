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

play_btn = tkk.Button(root, image=play)
play_btn.place(x=700, y=700)

# przycisk Info


def new_wind():
    extra_window = tkk.Toplevel(root)
    zas = Label(extra_window, text="ZASADY", width = 8, height= 2, font=('Times New Roman', 20, 'bold')).place(x= 310,y= 120)
    zasady_gry = Label(extra_window, text = "\nGra milionerzy polega na tym, aby \n odpowiedzieć poprawnie na 12 pytań, za\n każde pytanie jest dane suma pieniędzy. \n W grze są 2 progi gwarantowane \n 1000 pln i 40000 pln.\nW każdej rundzie uczestnik \n dostanie pytanie oraz cztery \n odpowiedzi, spośród których musi \n wybrać jedną właściwą. Każdy \n zawodnik ma prawo do wykorzystania \n trzech kół ratunkowych \n w dowolnym czasie gry.\n",
                        width=35,height=15, font=('Times New Roman', 20, 'bold')).place(x= 100,y= 270)
    kolorat1 = Label(extra_window, text ="koło ratunkowe, które eliminuje dwie błędne odpowiedzi", width=50,height=3, font=('Times New Roman', 20, 'bold')).place(x= 1000,y= 150)
    kolorat2 = Label(extra_window, text ="koło ratunkowe, które elimunuje jedną złą odpowiedź", width=50,height=3, font=('Times New Roman', 20, 'bold')).place(x= 1000,y= 500)
    kolorat3 = Label(extra_window, text ="koło ratunkowe, które wskazuje poprawną odpowiedź", width=50, height=3, font=('Times New Roman', 20, 'bold')).place(x= 1000,y= 850)

    kolo1 = tkk.PhotoImage(extra_window, file = "guzik-50na50.png")

    kl1 = tkk.Label(extra_window, image=kolo1)
    kl1.place(x=700, y=100)

    kolo2 = tkk.PhotoImage(extra_window, file = "guzik-eliminacja1zlejodp.png")

    kl2 = tkk.Label(extra_window, image=kolo2)
    kl2.place(x=700, y=450)

    kolo3 = tkk.PhotoImage(extra_window, file = "guzik-teldoprzyj.png")

    kl3 = tkk.Label(extra_window, image=kolo3)
    kl3.place(x=700, y=800)

info = tkk.PhotoImage(file="guzik-informacje.png")

info_btn = tkk.Button(root, image=info, command=new_wind)
info_btn.place(x=1685, y=770)





                       
root.mainloop()

