from tkinter import * # To import all I use *

root = Tk()
root.resizable(0, 0) # To disable maximize button!

root.title("CalcGuiPY")
root.iconbitmap('C:\CalcGuiPY\Icon\calc.ico') # To add your icon to the widget
root.configure(bg="black") # To set background to black color



e = Entry(root, width=10, borderwidth=0, bg="Black", fg="white", font=('Arial 35'), justify='center') # To making entry text/box bigger I add font size and to center I justify!
e.grid(row=0, column=0, columnspan=4, padx=15, pady=15)



def button_press(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


# Define Buttons
# I use Lambda in order to as button_press(1), without lambda it will not work in tkinter!
# For color code please visit : https://www.wikipython.com/tkinter-ttk-tix/summary-information/colors/

button_1 = Button(root, text="1", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(1)) 
button_2 = Button(root, text="2", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(2))
button_3 = Button(root, text="3", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(3))
button_4 = Button(root, text="4", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(4))
button_5 = Button(root, text="5", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(5))
button_6 = Button(root, text="6", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(6))
button_7 = Button(root, text="7", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(7))
button_8 = Button(root, text="8", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(8))
button_9 = Button(root, text="9", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=40, pady=20, bg="Black", fg="white", command=lambda: button_press(9))
button_0 = Button(root, text="0", font=('Bold'), activebackground="LightSteelBlue4", activeforeground="White", borderwidth=3, padx=41, pady=20, bg="Black", fg="white", command=lambda: button_press(0))
button_add = Button(root, text="+", font=('Bold'), activebackground="olive drab", activeforeground="White", borderwidth=3, width=4, padx=42, pady=20, bg="Black", fg="white", command=button_add)
button_equal = Button(root, text="=", font=('Bold'), activebackground="Dodgerblue3", activeforeground="White", borderwidth=3, width=4, padx=41.5, pady=20, bg="Black", fg="white", command=button_equal)
button_clear = Button(root, text="Clear", font=('Bold'), activebackground="IndianRed", activeforeground="White", borderwidth=3, width=4, padx=42, pady=20, bg="Black", fg="white", command=button_clear)
button_subtract = Button(root, text="-", font=('Bold'), activebackground="olive drab", activeforeground="White", borderwidth=3, width=4, padx=42, pady=20, bg="Black", fg="white", command=button_subtract)
button_multiply = Button(root, text="*", font=('Bold'), activebackground="olive drab", activeforeground="White", borderwidth=3, padx=42, width=1, pady=20, bg="Black", fg="white", command=button_multiply)
button_divide = Button(root, text="/", font=('Bold'), activebackground="olive drab", activeforeground="White", borderwidth=3, padx=42, width=1, pady=20, bg="Black", fg="white", command=button_divide)

# Placed the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=1, column=3)
button_add.grid(row=2, column=3)
button_equal.grid(row=4, column=3,)

button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4,column=1)
button_divide.grid(row=4, column=2)




root.mainloop()