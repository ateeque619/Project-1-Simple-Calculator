from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e) # to check error in console
                value="error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else: 
        scvalue.set(scvalue.get() + text)
        screen.update()
        # update function will force the screen Entry widget to update with new value

root = Tk()
root.geometry("396x580")
root.resizable(False,False)
root.title("Simple Calculator by Mohammed Ateeq")  
root.wm_iconbitmap("calculator.ico")

# creating string variable
# StringVar()’ is used to get the instance of the input field:
scvalue = StringVar()
scvalue.set("")

# Use the Frame widget to create a frame for the screen:
input_frame = Frame(root, bd=0, highlightbackground="dark grey", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP, fill=X)

# Created Entry widget inside the input_frame. Output aligned to the  right:
screen = Entry(input_frame, textvar=scvalue,bg="light grey",  font="lucida 40 bold", justify=RIGHT)
screen.grid(row=0, column=0, padx=1, pady=1)
screen.pack(ipady=10, fill=X)

# Create a separate Frame below the input field, which will include buttons positioned in rows inside the frame:
# first row includes 4 buttons, ‘7’, ‘8’, ‘9’ and ‘divide:
f1 = Frame(root, bg="dark grey")
f1.pack()

seven = Button(f1, text="7",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
seven.grid(row = 0, column = 0, padx = 1, pady = 1)
seven.bind("<Button-1>", click)

eight = Button(f1, text="8",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
eight.grid(row = 0, column = 1, padx = 1, pady = 1)
eight.bind("<Button-1>", click)

nine = Button(f1, text="9",bg="light grey", fg="black",cursor = "hand2", width=3,height=1, font="lucida 35 bold")
nine.grid(row = 0, column = 2, padx = 1, pady = 1)
nine.bind("<Button-1>", click)

divide = Button(f1, text="/", bg="light grey", fg="red",cursor = "hand2", width=3,height=1, font="lucida 35 bold")
divide.grid(row=0, column=3, padx=1, pady=1)
divide.bind("<Button-1>", click)

# second row includes 4 buttons, ‘4’, ‘5’, ‘6’ and ‘multiply:
f2 = Frame(root, bg="dark grey")
f2.pack()

four = Button(f2, text="4",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
four.grid(row = 1, column = 0, padx = 1, pady = 1)
four.bind("<Button-1>", click)

five = Button(f2, text="5",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
five.grid(row = 1, column = 1, padx = 1, pady = 1)
five.bind("<Button-1>", click)

six = Button(f2, text="6",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
six.grid(row = 1, column = 2, padx = 1, pady = 1)
six.bind("<Button-1>", click)

multiply = Button(f2, text="*",bg="light grey", fg="red",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
multiply.grid(row=1, column=3,padx=1, pady=1)
multiply.bind("<Button-1>", click)

# third row includes 4 buttons, ‘1’, ‘2’, ‘3’ and ‘minus:
f3 = Frame(root, bg="dark grey")
f3.pack()

one = Button(f3, text="1",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
one.grid(row=2, column=0, padx=1, pady=1)
one.bind("<Button-1>", click)

two = Button(f3, text="2",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
two.grid(row=2, column=1, padx=1, pady=1)
two.bind("<Button-1>", click)

three = Button(f3, text="3",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
three.grid(row=2, column=2, padx=1, pady=1)
three.bind("<Button-1>", click)

minus = Button(f3, text="-",bg="light grey", fg="red",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
minus.grid(row=2, column=3,padx=1, pady=1)
minus.bind("<Button-1>", click)

# fourth row includes 4 buttons, ‘0’, ‘.’, ‘00’ and ‘plus:
f4 = Frame(root, bg="dark grey")
f4.pack()

zero = Button(f4, text="0",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
zero.grid(row = 3, column = 0, padx = 1, pady = 1)
zero.bind("<Button-1>", click)

point = Button(f4, text=".",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
point.grid(row = 3, column = 1, padx = 1, pady = 1)
point.bind("<Button-1>", click)

dzero = Button(f4, text="00",bg="light grey", fg="black",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
dzero.grid(row = 3, column = 2, padx = 1, pady = 1)
dzero.bind("<Button-1>", click)

plus = Button(f4, text="+",bg="light grey", fg="red",cursor = "hand2", width=3, height=1, font="lucida 35 bold")
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
plus.bind("<Button-1>", click)

# fifth row includes 2 buttons, clear and equals:
f5 = Frame(root, bg="dark grey")
f5.pack()

clear = Button(f5, text="C",bg="light grey", fg="red",cursor = "hand2", padx=60, height=1, font="lucida 35 bold")
clear.grid(row = 4, column = 0, columnspan=2, padx = 1, pady = 1)
clear.bind("<Button-1>", click)

equals = Button(f5, text="=",bg="red", fg="black",cursor = "hand2", padx=64, height=1, font="lucida 35 bold")
equals.grid(row = 4, column = 2, columnspan=2, padx = 1, pady = 1)
equals.bind("<Button-1>", click)

root.mainloop()


# ‘ipady’ is internal padding that increases the height of the input field.
