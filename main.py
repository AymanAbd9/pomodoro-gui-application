from tkinter import *
import math
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
checkmark_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global checkmark_count

    root.after_cancel(timer)
    reps = 0
    checkmark_count = 0
    title_label.config(text='Timer', fg=GREEN)
    check_label.config(text='')
    canvas.itemconfig(timer_text, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    # if its long break time
    if reps % 8 == 0:
        title_label.config(text='Break', fg=RED)
        count_down(long_break_min)
    # if its work time
    elif reps % 2 != 0:
        title_label.config(text='Work', fg=GREEN)
        count_down(work_min)
    # if its short break time
    else:
        title_label.config(text='Break', fg=PINK)
        count_down(short_break_min)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global checkmark_count
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    # change the format of the minutes to two digits if its one digit
    if len(str(count_min)) == 1:
        count_min = "0" + str(count_min)

    # change the format of the seconds to two digits if its one digit
    if len(str(count_sec)) == 1:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        # if a work is done, add one checkmark
        if reps % 2 == 0:
            checkmark_count += 1
            check_label.config(text=checkmark_count * '✔')

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Pomodoro')
root.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1, padx=20, pady=20)



start_button = Button(text='start', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='reset', command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(text='', bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

root.mainloop()
