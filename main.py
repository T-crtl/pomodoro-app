from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    title_label.config(text="Pomodoro")
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def star_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Break", fg=RED)   
    elif reps % 2 > 0:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="Break", fg=PINK)
            
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):

    minutes_count = math.floor(count / 60)
    second_count = count % 60
    if second_count < 10:
        second_count = f"0{second_count}"
    if minutes_count == 0:
        minutes_count = "00"
    canvas.itemconfig(timer_text, text=f"{minutes_count}:{second_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        star_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_pomodoro = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=image_pomodoro)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
title_label.grid(column=1, row=0)

button1 = Button(text="Start", highlightthickness=0, bd=0, command=star_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", highlightthickness=0, bd=0, command=timer_reset)
button2.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()



