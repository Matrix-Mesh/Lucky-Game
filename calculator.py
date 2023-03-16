from tkinter import * # Import everything from Tkinter module

root = Tk() # This is to create a basic window
root.geometry("500x700") # this is for the size of the window
root.title("Calculator")  # This is to set the title of the window
root.wm_iconbitmap("image.ico") #This is to set the icon
root.resizable(False,False) # this is to prevent from resizing the window

# 'btn_click' function : 
# This Function continuously updates the input field whenever you enter a number

def btn_click(item):
 global expression
 expression = expression + str(item)
 scvalue.set(expression)
 
#'bt_clear' function :This is used to clear the input field

def bt_clear():
    global expression 
    expression = "" 
    scvalue.set("")

# 'bt_equal':This method calculates the expression  present in input field
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    scvalue.set(result)
    expression = ""

expression = ""

# 'StringVar()' :It is used to get the instance of input field
scvalue = StringVar()
scvalue.set("")        # Setting the default value empty


# Creating buttons within Frames

f = Frame(root, width=3, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
f.pack(side=TOP)

screen = Entry(f ,textvariable=scvalue , font= "lucida 40 bold", width=50, bg="#eee", bd=0, justify=RIGHT)
screen.grid(row=0, column=0)
screen.pack(fill=X, ipadx=8 , padx=10, pady=10) #Taking Input

btns_frame = Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# Row 1

b9 = Button(btns_frame, text="9" ,padx=20 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click(9)).grid(row = 0, column = 0, padx = 1, pady = 1)

b8 = Button(btns_frame, text="8" , padx=20 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click(8)).grid(row = 0, column = 1, padx = 1, pady = 1)

b7 = Button(btns_frame, text="7" , padx=20 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click(7)).grid(row = 0, column = 2, padx = 1, pady = 1)

add = Button(btns_frame, text="+" , padx=28 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click("+")).grid(row = 0, column = 3, padx = 1, pady = 1)

# Row 2

b6 = Button(btns_frame, text="6" , padx=20 , pady=18, font="lucida 30 bold", command = lambda: btn_click(6)).grid(row = 1, column = 0, padx = 1, pady = 1)

b5 = Button(btns_frame, text="5" , padx=20 , pady=18, font="lucida 30 bold", command = lambda: btn_click(5)).grid(row = 1, column = 1 , padx = 1, pady = 1)

b4 = Button(btns_frame, text="4" , padx=20 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click(4)).grid(row = 1, column = 2, padx = 1, pady = 1)

sub = Button(btns_frame, text="-" , padx=31 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click("-")).grid(row = 1, column = 3, padx = 0, pady = 1)

# Row 3

b3 = Button(btns_frame, text="3" , padx=20 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click(3)).grid(row = 2, column = 0, padx = 1, pady = 1)
b2 = Button(btns_frame, text="2" , padx=20 , pady=18, font="lucida 30 bold", command = lambda: btn_click(2)).grid(row = 2, column = 1, padx = 1, pady = 1)
b1 = Button(btns_frame, text="1" , padx=20 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click(1)).grid(row = 2, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text="*" , padx=30 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click("*")).grid(row = 2, column = 3, padx = 0, pady = 1)

# Row 4

b0 = Button(btns_frame, text="0" , padx=69 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click(0)).grid(row = 3, column = 0, padx = 1, pady = 1 , columnspan=2)

dot= Button(btns_frame, text="." , padx=25 , pady=18, font="lucida 30 bold" , command = lambda: btn_click(".")).grid(row = 3, column = 2, padx = 0, pady = 0)

divide = Button(btns_frame, text="/" , padx=33 , pady=18, font="lucida 30 bold" ,command = lambda: btn_click("/")).grid(row = 3, column = 3, padx = 0, pady = 1)

# Row 5

clear = Button(btns_frame, text="C" , padx=113 , pady=18, font="lucida 30 bold" ,command = lambda: bt_clear()).grid(row = 4, column = 0,columnspan=3 ,padx = 0, pady = 0)

equal = Button(btns_frame, text="=" , padx=28, pady=18, font="lucida 30 bold" ,command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()
