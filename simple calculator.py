# ------------------------------------------
#   Program by Andrii C.
#
#
#
#   Version
#     0.1
#
# ------------------------------------------
from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)

entry = Entry(root, width=35, borderwidth=2)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# ----- CREATING THE FUNCTIONS -----
def add_into_entry(num):
    # add new symbols synchronized with the buttons
    entry.insert(END, num)


# ----- INITIALIZE THE SYMBOLS IN CALCULATOR -----
symbols = {"minus": "-",
           "plus": "+",
           "multiplication": "*",
           "equal": "="
           }
symbols = globals()


def minus(symbol):
    first_num = entry.get()
    global f_num
    global math
    math = str("minus")
    f_num = int(first_num)

    entry.delete(0, END)


def multiplication(symbol):
    first_num = entry.get()
    global f_num
    global math
    math = str("multiplication")
    f_num = int(first_num)

    entry.delete(0, END)


def equal():
    # here we get the second number after first number:
    second_num = entry.get()
    entry.delete(0, END)

    # result for +
    if math == str("addition"):
        entry.insert(0, float(f_num + int(second_num)))

    # result for "-"
    if math == str("minus"):
        entry.insert(0, float(f_num - int(second_num)))

    # result for "*"
    if math == str("multiplication"):
        entry.insert(0, float(f_num * int(second_num)))

    # result for "/"
    if math == str("division"):
        entry.insert(0, float(f_num / int(second_num)))


def plus(symbol):
    # initializing the activity for adding symbol :
    first_num = entry.get()
    global f_num
    global math
    math = str("addition")
    f_num = int(first_num)

    entry.delete(0, END)


def division(symbol):
    first_num = entry.get()
    global f_num
    global math
    math = str("division")
    f_num = int(first_num)

    entry.delete(0, END)


def clear():
    # For that function we need just to remove all from the entry field
    entry.delete(0, END)


# ----- BUTTONS ------
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_into_entry(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_into_entry(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_into_entry(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_into_entry(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_into_entry(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_into_entry(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_into_entry(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_into_entry(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_into_entry(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_into_entry(0))
button_plus = Button(root, text="+", padx=39, pady=20, command=lambda: plus("+"))
button_minus = Button(root, text="-", padx=40, pady=20, command=lambda: minus("-"))
button_clear = Button(root, text="C", padx=20, pady=20, command=clear)
button_equal = Button(root, text="=", padx=20, pady=20, command=equal)
button_multiplication = Button(root, text="*", padx=21.5, pady=20, command=lambda: multiplication("*"))
button_division = Button(root, text="/", padx=21.5, pady=20, command=lambda: division("/"))

# ----- PLACEMENT THE BUTTONS -----
button_plus.grid(row=5, column=2)
button_minus.grid(row=5, column=0)
button_clear.grid(row=2, column=3)
button_division.grid(row=3, column=3)
button_multiplication.grid(row=4, column=3)
button_equal.grid(row=5, column=3)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)


root.mainloop()

