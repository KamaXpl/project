import random
import tkinter as tkk
from tkinter import *
import mysql.connector
from tkinter import messagebox


import MySQLdb

milionerzy = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="milionerzy")        # name of the data base



cur = milionerzy.cursor()


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
  
 # Koła ratunkowe
    


    for i in range(12):
        def pyta():
           cur.execute("Select * from pyt inner join odp on id=id1;")
           pytanie = cur.fetchall()
           pytanie = random.sample(pytanie, 12)
    
        def odpA():
           cur.execute("Select A from odp inner join pyt on id1=id;")
           A = cur.fetchall()
           A = random.sample(A, 12)
    
        def odpB():
           cur.execute("Select B from odp inner join pyt on id1=id;")
           B = cur.fetchall()
           B = random.sample(B, 12)
    
        def odpC():
            cur.execute("Select C from odp inner join pyt on id1=id;")
            C = cur.fetchall()
            C = random.sample(C, 12)
     
        def odpD():
            cur.execute("Select D from odp inner join pyt on id1=id;")
            D = cur.fetchall()
            D = random.sample(D, 12)


        def odp_pop():
            cur.execute("Select Poprawna_odp from odp inner join pyt on id1=id;")
            popr = cur.fetchall()
            popr = random.sample(popr, 12)



        Pytanie1 = Label(play_window, text=pyta).place(x=300, y=350, width=700, height=200)
        A1 = Button(play_window, text=odpA).place(x=50, y=600, width=600, height=200)
        B2 = Button(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
        C3 = Button(play_window, text=odpC).place(x=50, y=800, width=600, height=200)
        D4 = Button(play_window, text=odpD).place(x=650, y=800, width=600, height=200)
        



        





        def p_na_p(): #pol na poł
          if odpA == odp_pop:
            B1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
            C1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
          if odpB == odp_pop:
            C1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
            D1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
          if odpC == odp_pop:
            D1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
            A1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
          if odpD == odp_pop:
            A1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
            B1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)

        def eliminacja(): #eliminacja1zlejodp
          if odpA == odp_pop:
            B1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
          if odpB == odp_pop:
            C1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
          if odpC == odp_pop:
            D1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
          if odpD == odp_pop:
            A1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)

        def tel():  #tel do przyjaciela
          if odpA == odp_pop:
            B1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
            C1 = Label(play_window, text=odpC).place(x=50, y=800, width=600, height=200)
            D1 = Label(play_window, text=odpD).place(x=650, y=800, width=600, height=200)
          if odpB == odp_pop:
            A1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
            C1 = Label(play_window, text=odpC).place(x=50, y=800, width=600, height=200)
            D1 = Label(play_window, text=odpD).place(x=650, y=800, width=600, height=200)
          if odpC == odp_pop:
            B1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
            A1 = Label(play_window, text=odpC).place(x=50, y=800, width=600, height=200)
            D1 = Label(play_window, text=odpD).place(x=650, y=800, width=600, height=200)
          if odpD == odp_pop:
            B1 = Label(play_window, text=odpB).place(x=650, y=600, width=600, height=200)
            C1 = Label(play_window, text=odpC).place(x=50, y=800, width=600, height=200)
            D1 = Label(play_window, text=odpD).place(x=650, y=800, width=600, height=200)

        kolo1 = tkk.PhotoImage(file = "guzik-50na50.png")
        kolo_1 = tkk.Button(play_window, image=kolo1, command=p_na_p)
        kolo_1.place(x=150, y=50)

        kolo2 = tkk.PhotoImage(file = "guzik-eliminacja1zlejodp.png")
        kolo_2 = tkk.Button(play_window,image=kolo2, command=eliminacja)
        kolo_2.place(x=550, y=50)

        kolo3 = tkk.PhotoImage(file = "guzik-teldoprzyj.png")
        kolo_3 = tkk.Button(play_window, image=kolo3, command=tel)
        kolo_3.place(x=950, y=50)



        
        

    

        play_window.mainloop()


play = tkk.PhotoImage(file="guzik-zagraj.png")

play_btn = tkk.Button(root, image=play, command=gra)
play_btn.place(x=700, y=700)

                       
root.mainloop()


