import random
import tkinter as tkk
from tkinter import *
import mysql.connector


import MySQLdb

milionerzy = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="milionerzy")        # name of the data base


cur = milionerzy.cursor()
zestawy = [
cur.execute("SELECT Pytania FROM pyt WHERE id BETWEEN 1 AND 12"), 
cur.execute("SELECT Pytania FROM pyt WHERE id BETWEEN 13 AND 24"),
cur.execute("SELECT Pytania FROM pyt WHERE id BETWEEN 25 AND 36"),
cur.execute("SELECT Pytania FROM pyt WHERE id BETWEEN 37 AND 48")]

zes_wyb = random.choices(zestawy)
print(milionerzy)

root = tkk.Tk()
root.geometry('1920x1080')
root.configure(bg="black")


# wejscie do gry

bg = tkk.PhotoImage(file = "milionerzy1.png")

play_img = tkk.Label(image=bg)
play_img.place(x=0, y=0)

# przycisk Info

def informacje():
    extra_window = tkk.Toplevel()
    extra_window.geometry('1920x1080')
    bg2 = tkk.PhotoImage(file = "milionerzy1.png")
    bg3 = tkk.Label(extra_window, image=bg2)
    bg3.place(x=0, y=0)
    zas = Label(extra_window, text=" ZASADY", bg="#2c397f", highlightthickness=10, width = 8, height= 2, font=('Times New Roman', 20, 'bold')).place(x= 270,y= 220)
    zasady_gry = Label(extra_window, text = "\nGra milionerzy polega na tym, aby \n odpowiedzieć poprawnie na 12 pytań, za\n każde pytanie jest dana suma pieniędzy. \n W grze są 2 progi gwarantowane \n 1000 pln i 40000 pln.\nW każdej rundzie uczestnik \n dostanie pytanie oraz cztery \n odpowiedzi, spośród których musi \n wybrać jedną właściwą. Każdy \n zawodnik ma prawo do wykorzystania \n trzech kół ratunkowych \n w dowolnym czasie gry.\n",
                        bg="#2c397f", highlightthickness=10, width=35,height=15, font=('Times New Roman', 20, 'bold')).place(x= 60,y= 350)
    kolorat1 = Label(extra_window, text ="koło ratunkowe, które eliminuje dwie błędne odpowiedzi", bg="#2c397f", highlightthickness=10,  width=50,height=3, font=('Times New Roman', 20, 'bold')).place(x= 1000,y= 300)
    kolorat2 = Label(extra_window, text ="koło ratunkowe, które elimunuje jedną złą odpowiedź", bg="#2c397f", highlightthickness=10, width=50,height=3, font=('Times New Roman', 20, 'bold')).place(x= 1000,y= 570)
    kolorat3 = Label(extra_window, text ="koło ratunkowe, które wskazuje poprawną odpowiedź", bg="#2c397f", highlightthickness=10, width=50, height=3, font=('Times New Roman', 20, 'bold')).place(x= 1000,y= 850)

    image1= tkk.PhotoImage(file = "guzik-50na50.png")
    kl1 = tkk.Label(extra_window, image=image1)
    kl1.place(x=700, y=250)

    image2 = tkk.PhotoImage(file = "guzik-eliminacja1zlejodp.png")
    kl2 = tkk.Label(extra_window,image=image2)
    kl2.place(x=700, y=525)

    image3 = tkk.PhotoImage(file = "guzik-teldoprzyj.png")
    kl3 = tkk.Label(extra_window, image=image3)
    kl3.place(x=700, y=800)

    extra_window.mainloop()


info = tkk.PhotoImage(file="guzik-informacje.png")

info_btn = tkk.Button(root, image=info, command=informacje)
info_btn.place(x=1685, y=770)

# przycisk Zagraj 

def gra():
    play_window = tkk.Toplevel()
    play_window.geometry('1920x1080')
    bg4 = tkk.PhotoImage(file = "milionerzy2.png")
    bg5 = tkk.Label(play_window, image=bg4)
    bg5.place(x=0, y=0)
    tab1 = tkk.PhotoImage(file = "tablica.png")
    tab_1 = tkk.Label(play_window, image=tab1)
    tab_1.place(x=1300,y=-40)

    play_window.mainloop()


play = tkk.PhotoImage(file="guzik-zagraj.png")

play_btn = tkk.Button(root, image=play, command=gra)
play_btn.place(x=700, y=700)

                       
root.mainloop()


