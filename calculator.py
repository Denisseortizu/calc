#Python program to create a simple GUI
# using Tkinter
from tkinter import *

#Globaly declare expression variable

expression = ""

# Function to update expression 
# in the text entry box
def press(num):
    global expression

    expression = expression + str(num)

    #Update expression variable
    equation.set(expression)


#Driver code
if __name__ == "__main__":

    #We create Gui Window
    gui = TK()

    #Set bkgd colour for gui
    gui.configure(background="light blue")
    #Set tittle of gui
    gui.tittle("Denisse Calculator")
    #Set configuration of gui
    gui.geometry("270x150")

    #StringVar() is variable class
    equation = StringVar()

    #create the text entry box for showing the expression
    expression_field = Entry(gui, textvariable=equation)

    #We use the grid method used for placing the widgets
    expression_field.grid(columnspan=4, ipadx=70)

    #Create buttons using the grid method

    #Numbers buttons
    button1 = Button(gui, text=' 1 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(1), height=1, width=7)  
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(2), height=1, width=7)  
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(3), height=1, width=7)  
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(4), height=1, width=7)  
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(5), height=1, width=7)  
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(6), height=1, width=7)  
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(7), height=1, width=7)  
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(8), height=1, width=7)  
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(9), height=1, width=7)  
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg=' black ', bg=' grey ', 
                     command=lambda: press(0), height=1, width=7)  
    button0.grid(row=5, column=0)

    #Oper buttons

    minus = Button(gui, text=' - ', fg='black', bg='grey',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

