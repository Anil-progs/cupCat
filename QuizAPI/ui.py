
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quezbrain:QuizBrain):
        self.quiz=quezbrain
        self.window=Tk()
        self.window.title("Quiz Game")
        self.window.configure(bg=THEME_COLOR)
        self.window.geometry("400x600")

        self.convas=Canvas(height=250,width=300,bg="white")
        self.question=self.convas.create_text(150,125,text="Something is nessessary",fill=THEME_COLOR,
                                              font=("Calibre",10),
                                              width=280)
        self.convas.place(x=50,y=100)

        image_true=PhotoImage(file="true.png")
        self.button_true=Button(image=image_true, command=self.the_right_answer,highlightthickness=0)
        self.button_true.place(x=30,y=400)

        image_false=PhotoImage(file="false.png")
        self.button_false=Button(image=image_false,command=self.the_range_answer,highlightthickness=0)
        self.button_false.place(x=240,y=400)

        self.label_score=Label(text=f"Score:0",bg=THEME_COLOR)
        self.label_score.place(x=240,y=30)
        self.next_question_in_here()
        self.window.mainloop()
    def next_question_in_here(self):
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.convas.itemconfig(self.question,text=q_text)
        else:
            self.convas.itemconfig(self.question,text="You are reached the end of quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
    def the_right_answer(self):
        self.get_feadback(self.quiz.check_answer("True"))
    def the_range_answer(self):
        is_right=self.quiz.check_answer("False")
        self.get_feadback(is_right)

    def change_color(self):
        self.convas.configure(bg="white")
    def get_feadback(self,is_right):
        if is_right:
            self.convas.configure(bg="green")
        else:
            self.convas.configure(bg="red")

        self.window.after(1000, self.change_color)
        self.window.after(1000,self.next_question_in_here)













