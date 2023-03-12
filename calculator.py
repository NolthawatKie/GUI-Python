from tkinter import *

root = Tk()
root.title("Calculator")

content = ""
text_input = StringVar(value="0")


def btnPress(number):
    global content
    content += str(number)
    text_input.set(content)


def calculcate():
    global content
    result = float(eval(content))
    text_input.set(result)


def clear():
    text_input.set("0")


# Display
display = Entry(textvariable=text_input, font=(
    'san serif', 30, 'bold'), fg='black', bg='light gray', justify='right')
display.grid(columnspan=4)

# Row 1
btn7 = Button(text="7", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(7)).grid(row=1, column=0)
btn8 = Button(text="8", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(8)).grid(row=1, column=1)
btn9 = Button(text="9", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(9)).grid(row=1, column=2)
btnc = Button(text="C", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=clear).grid(row=1, column=3)

# Row 2
btn4 = Button(text="4", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(4)).grid(row=2, column=0)
btn5 = Button(text="5", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(5)).grid(row=2, column=1)
btn6 = Button(text="6", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(6)).grid(row=2, column=2)
btnplus = Button(text="+", font=('san serif', 30, 'bold'),
                 padx=35, pady=15, command=lambda: btnPress("+")).grid(row=2, column=3)

# Row 3
btn1 = Button(text="1", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(1)).grid(row=3, column=0)
btn2 = Button(text="2", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(2)).grid(row=3, column=1)
btn3 = Button(text="3", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(3)).grid(row=3, column=2)
btnminus = Button(text="-", font=('san serif', 30, 'bold'),
                  padx=38, pady=15, command=lambda: btnPress("-")).grid(row=3, column=3)

# Row 4
btn0 = Button(text="0", font=('san serif', 30, 'bold'),
              padx=35, pady=15, command=lambda: btnPress(0)).grid(row=4, column=0)
btndot = Button(text=".", font=('san serif', 30, 'bold'),
                padx=40, pady=15, command=lambda: btnPress(".")).grid(row=4, column=1)
btndivide = Button(text="/", font=('san serif', 30, 'bold'),
                   padx=40, pady=15, command=lambda: btnPress("/")).grid(row=4, column=2)
btnmultiply = Button(text="*", font=('san serif', 30, 'bold'),
                     padx=38, pady=15, command=lambda: btnPress("*")).grid(row=4, column=3)

# Row 5
btnequal = Button(text="=", font=('san serif', 30, 'bold'),
                  padx=88, pady=15, command=calculcate).grid(row=5, column=0, columnspan=2)
btnopen = Button(text="(", font=('san serif', 30, 'bold'),
                 padx=40, pady=15, command=lambda: btnPress("(")).grid(row=5, column=2)
btnclose = Button(text=")", font=('san serif', 30, 'bold'),
                  padx=40, pady=15, command=lambda: btnPress(")")).grid(row=5, column=3)


root.mainloop()
