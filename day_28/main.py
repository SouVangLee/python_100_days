from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
SECONDS = 60
reps = 0
timer = None


# Countdown mechanism
def count_down(count):
    count_min = math.floor(count / SECONDS)
    count_sec = count % SECONDS

    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_marks.config(text=marks)


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * SECONDS
    short_break_sec = SHORT_BREAK_MIN * SECONDS
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break!", fg=RED)
        # count_down(long_break_sec)
        count_down(2)
    elif reps % 2 == 0:
        timer_label.config(text="Break!", fg=RED)
        # count_down(short_break_sec)
        count_down(2)
    else:
        timer_label.config(text="Work!")
        # count_down(work_sec)
        count_down(2)


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")


# Creating window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

# Create canvas and add image
img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

# Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
timer_label.config(fg=PINK, bg=GREEN)
timer_label.grid(row=0, column=1)

# reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

# start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# check mark label
check_marks = Label(text="", fg=PINK, bg=GREEN, font=(FONT_NAME, 24, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
