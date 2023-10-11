import MySQLdb
from tkinter import *
from tkinter import messagebox
import hashlib
import random
class Quiz:
    def __init__(self, master, u):
        self.user = u
        global mQuiz
        mQuiz = master
        self.master = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Online Quiz - Registration")
        self.master.config(bg="azure")
        global f1
        f = Frame(self.master, height=1080, width=1920, bg="azure", relief="ridge", bd=20)
        conn = MySQLdb.connect(host='localhost', database='world', user='root', password='root')
        cursor = conn.cursor()

        global l1, answerstemp
        global questions
        questions = []
        global options
        options = []
        global answers
        answers = []
        answerstemp = []
        s1 = set()

        while len(s1) < 10:
            strQ = ""
            strA = ""
            id = random.randint(1, 30)
            s1.add(id)

        while len(s1) > 0:
            s = "select qstn from questions where QID=%d"
            id = s1.pop()
            arg = (id)
            cursor.execute(s % arg)
            strQ = strQ.join(list(cursor.fetchone()))
            questions.append(strQ)

            s = "select opA,opB,opC,opD from questions where QID=%d"
            arg = (id)
            cursor.execute(s % arg)
            options.append(list(cursor.fetchone()))

            s = "select ans from questions where QID=%d"
            arg = (id)
            cursor.execute(s % arg)
            l = list(cursor.fetchone())
            answerstemp.append(l)

        mydict = {}
        for i in range(10):
            mydict[questions[i]] = options[i]
        for i in range(len(answerstemp)):
            answers.append(answerstemp[i][0])

        print("DEBUG: Answers= ", answers)

        cursor.close()
        conn.close()
        l1 = {}
        for i in range(10):
            l1[i] = 0

        f.propagate(0)
        f.pack()
        self.qno = 0
        self.score1 = 0
        self.ques = self.create_q(f, self.qno)
        self.opts = self.create_options(f)
        self.display_q(self.qno)
        self.Back = Button(f, text="<- Back", width=15, height=3, fg="royalblue4", bg="snow2",
                           font=("Helvetica", 10, "bold italic"), command=self.back).place(x=100, y=325)
        self.Next = Button(f, text="Next ->", width=15, height=3, fg="royalblue4", bg="snow2",
                           font=("Helvetica", 10, "bold italic"), command=self.next).place(x=250, y=325)
        self.submit = Button(f, text="Submit", width=34, height=2, fg="ghost white", bg="DeepSkyBlue2",
                             font=("Helvetica", 10, "bold italic"), command=self.Submit).place(x=100, y=400)

        imgID = random.randint(1, 4)
        filestr = "E:\OSTL\MiniProject\Resources\\" + str(imgID) + ".png"
        self.quizImg = PhotoImage(file=filestr)
        img = Label(f, image=self.quizImg, bg="azure")
        img.place(x=700, y=200)

    def create_q(self, master, qno):
        qLabel = Label(master, text=questions[qno], bg='azure', font=("Times New Roman", 20))
        qLabel.place(x=30, y=70)
        return qLabel

    def create_options(self, master):
        b_val = 0
        b = []
        ht = 85
        self.opt_selected = IntVar()
        while b_val < 4:
            btn = Radiobutton(master, text="", variable=self.opt_selected, value=b_val + 1, bg='azure',
                              font=("Times New Roman", 20))
            b.append(btn)
            ht = ht + 40
            btn.place(x=30, y=ht)
            b_val = b_val + 1
        return b

    def display_q(self, qno):
        b_val = 0
        self.ques['text'] = str(qno + 1) + ". " + questions[qno]
        for op in options[qno]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def next(self):
        self.qno += 1

        if self.qno >= len(questions):
            self.qno -= 1
            messagebox.showwarning("Warning", "You are at the end.Press Submit to proceed")
        else:
            l1[self.qno - 1] = self.opt_selected.get()
            self.opt_selected.set(l1[(self.qno)])
            self.display_q(self.qno)

    def back(self):
        l1[self.qno] = self.opt_selected.get()
        self.qno -= 1
        if self.qno < 0:
            self.qno += 1
            messagebox.showerror("Error", "You are already in the start!!!")
        else:
            self.display_q(self.qno)
            c = l1[self.qno]
            self.opt_selected.set(c)

    def Submit(self):
        l1[self.qno] = self.opt_selected.get()
        x = 0
        y = True
        for i in range(10):
            if (l1[i] == 0):
                x += 1
        if (x > 0 and x != 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(
                x) + " questions, Are you sure you want to submit?, You won't be able to make changes again")
        elif (x == 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(
                x) + " question, Are you sure you want to submit?, You won't be able to make changes again")
        if (y == True or x == 0):
            s = 0
            for i in range(10):
                if (l1[i] == answerstemp[i][0]):
                    s = s + 1
            print("DEBUG: Score: ", s)

        conn = MySQLdb.connect(host='localhost', database='world', user='root', password='root')
        cursor = conn.cursor()
        q = "update reg set score='%d' where uname= '%s'"
        arg = (s, self.user)
        cursor.execute(q % arg)
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Score", "Your Score is: " + str(s) + "/10")
        mQuiz.destroy()
