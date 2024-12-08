from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        """ CANVAS """

        self.score_label = Label(self.window, text="Score:",fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text ="Hello World",
            width= 200,             # wraps the questions in the canvas
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        """ True Button """
        self.tick_image = PhotoImage(file="images/true.png")
        self.tick = Button(image=self.tick_image, highlightthickness=0 , command=self.pressed_true)
        self.tick.grid(row=2, column=0)

        """ False Button """
        self.cross_image = PhotoImage(file="images/false.png")
        self.cross = Button(image=self.cross_image, highlightthickness=0, command=self.pressed_false )
        self.cross.grid(row=2, column=1)

        self.get_next_question()        # ensures to run the function before mainloop()
        self.window.mainloop()

    """ gets questions and show them in the canvas """
    def get_next_question(self):
        self.canvas.config(bg="white")                  # resets bg to white after 1 sec of pushing button
        if self.quiz.still_has_questions():             # calls function that checks if questions remains
            self.score_label.config(text=f"Score: {self.quiz.score} of {self.quiz.question_number + 1}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Game Over", font=("Arial", 40, "bold"))    # prints game over after questions runs out
            self.tick.config(state="disabled")              # disables the button after game over
            self.cross.config(state="disabled")

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))      # If answer true, calls feedback with args
    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))     # if answer false, calls feedback with args

    def give_feedback(self, is_right):        # give feedback after clicking the button
        if is_right:
            self.canvas.config( bg="green")     # flashes green for 1 second if correct
        else:
            self.canvas.config( bg="red")       # flashes red for 1 second if correct
        self.window.after(1000, self.get_next_question)         # changes to default color after 1 second
