
from tkinter import *

expression = "" 


# Function to update expression 
# in the text entry box 
def press(num): 
	# point out the global expression variable 
	global expression 

	# concatenation of string 
	expression = expression + str(num) 

	# update the expression by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global expression 

		# eval function evaluate the expression 
		# and str function convert the result 
		# into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialize the expression variable 
		# by empty string 
		expression = "" 

	# if error is generate then handle 
	# by the except block 
	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	bidun = Tk() 

	# set the background colour of GUI window 
	bidun.configure(background="light green") 

	# set the title of GUI window 
	bidun.title(" Calculator") 

	# set the configuration of GUI window 
	bidun.geometry("280x240") 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression . 
	expression_field = Entry(bidun,bg='aqua',font='bold', textvariable=equation) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(columnspan=4, ipadx=25)

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button7 = Button(bidun, text=' 7 ', fg='white', bg='black', 
					command=lambda: press(7), height=2, width=8) 
	button7.grid(row=2, column=0) 
	button8 = Button(bidun, text=' 8 ', fg='white', bg='black', 
					command=lambda: press(8), height=2, width=8) 
	button8.grid(row=2, column=1) 

	button9 = Button(bidun, text=' 9 ', fg='white', bg='black', 
					command=lambda: press(9), height=2, width=8) 
	button9.grid(row=2, column=2) 

	button4 = Button(bidun, text=' 4 ', fg='white', bg='black', 
					command=lambda: press(4), height=2, width=8) 
	button4.grid(row=3, column=0) 

	button5 = Button(bidun, text=' 5 ', fg='white', bg='black', 
					command=lambda: press(5), height=2, width=8) 
	button5.grid(row=3, column=1) 
	button6 = Button(bidun, text=' 6 ', fg='white', bg='black', 
					command=lambda: press(6), height=2, width=8) 
	button6.grid(row=3, column=2) 
	button1 = Button(bidun, text=' 1 ', fg='white', bg='black', 
					command=lambda: press(1), height=2, width=8) 
	button1.grid(row=4, column=0) 
	button2 = Button(bidun, text=' 2 ', fg='white', bg='black', 
					command=lambda: press(2), height=2, width=8) 
	button2.grid(row=4, column=1) 
	button3 = Button(bidun, text=' 3 ', fg='white', bg='black', 
					command=lambda: press(3), height=2, width=8) 
	button3.grid(row=4, column=2) 
	button0 = Button(bidun, text=' 0 ', fg='white', bg='black', 
					command=lambda: press(0), height=2, width=8) 
	button0.grid(row=5, column=0) 
	Decimal= Button(bidun, text='.', fg='white', bg='black', 
					command=lambda: press('.'), height=2, width=8) 
	Decimal.grid(row=5, column=1) 
	percentage = Button(bidun, text='%',fg='white',bg='black',
	         command=lambda:press('%'),height=2, width=8) 
	percentage.grid(row=5,column=2)
	divide = Button(bidun, text=' / ', fg='white', bg='black', 
					command=lambda: press("/"), height=2, width=8) 
	divide.grid(row=2, column=3) 
	multiply = Button(bidun, text=' * ', fg='white', bg='black', 
					command=lambda: press("*"), height=2, width=8) 
	multiply.grid(row=3, column=3) 
	minus = Button(bidun, text=' - ', fg='white', bg='black', 
				command=lambda: press("-"), height=2, width=8) 
	minus.grid(row=4, column=3) 
	plus = Button(bidun, text=' + ', fg='white', bg='black', 
				command=lambda: press("+"), height=2, width=8) 
	plus.grid(row=5, column=3) 
	equal = Button(bidun, text=' = ', fg='white', bg='blue', 
				command=equalpress, height=2, width=8) 
	equal.grid(row=7, column=3) 
	clear = Button(bidun, text='Clear', fg='black', bg='red', 
				command=clear, height=2, width=8) 
	clear.grid(row=7, column='0') 
	bidun.mainloop() 
