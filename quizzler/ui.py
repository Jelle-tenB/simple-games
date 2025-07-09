from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="hello",
            font=('Courier', 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {0}", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        true_img = PhotoImage(file="quizzler/images/true.png")
        self.true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row=2, padx=20, pady=20)

        false_img = PhotoImage(file="quizzler/images/false.png")
        self.false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
