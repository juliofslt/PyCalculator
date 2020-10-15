from tkinter import *

def calculator():
	# Configuracion de ventana raiz
	root = Tk()

	root.title('Calculadora')
	root.resizable(0,0)


	# Variables
	result = ''
	entrada = StringVar(value = ' ')
	op = ''


	# Functions

	# Reset entry field and result
	def clear():
		nonlocal result
		clear_entry()
		result = ''

	# Clear entry field
	def clear_entry():
		entrada.set(' ')

	# Button "+/-"
	def minus_p():
		if entrada.get()[0] != '-':
			entry.insert(0, '-')
			entry.delete(1,2)
		elif entrada.get()[0] == '-':
			entry.delete(0,1)
			entry.insert(0, ' ')

	# Math operations
	def ope(button):
		nonlocal result
		nonlocal op
		nonlocal entrada

		try:
			
			# Result
			if button['text'] == "=":
				result += f'({entrada.get()})'
				print(result)
				entrada.set(eval(result))
				result = ''
				op = ''
			
			# Any other math op
			else:
				op = button['text']
				result += f'({entrada.get()}) {op} '
				print(result)
				clear_entry()
		
		# Non-valid inputs
		except:
			print(result)
			entrada.set('NOPE')


	# Create widgets

	# Entry field
	entry = Entry(root,font = ("Roboto", 20), width = 28, textvariable = entrada)
	entry.grid(row = 0, column = 0, columnspan = 4)
	# entry.delete(0, END)


	# Math operator buttons

	ac = Button(root, text = 'ac', width = 21, command = clear)
	ac.grid(row = 1, column = 0, columnspan = 2)


	minus_plus = Button(root, text = '+/-', width = 10, command = minus_p)
	minus_plus.grid(row = 1, column = 2)

	plus = Button(root, text = '+', width = 10, command = lambda: ope(plus))
	plus.grid(row = 1, column = 3)

	minus = Button(root, text = '-', width = 10, command = lambda: ope(minus))
	minus.grid(row = 2, column = 3)

	mult = Button(root, text = '*', width = 10, command = lambda: ope(mult))
	mult.grid(row = 3, column = 3)

	div = Button(root, text = '/', width = 10, command = lambda: ope(div))
	div.grid(row = 4, column = 3)

	eq = Button(root, text = '=', width = 10, command = lambda: ope(eq))
	eq.grid(row = 5, column = 3)


	# Number buttons

	one = Button(root, text = '1', width = 10, command = lambda: entry.insert(END, one['text']))
	one.grid(row = 4, column = 0)
	two = Button(root, text = '2', width = 10, command = lambda: entry.insert(END, two['text'])) 
	two.grid(row = 4, column = 1)
	three = Button(root, text = '3', width = 10, command = lambda: entry.insert(END, three['text'])) 
	three.grid(row = 4, column = 2)
	four = Button(root, text = '4', width = 10, command = lambda: entry.insert(END, four['text'])) 
	four.grid(row = 3, column = 0)
	five = Button(root, text = '5', width = 10, command = lambda: entry.insert(END, five['text'])) 
	five.grid(row = 3, column = 1)
	six = Button(root, text = '6', width = 10, command = lambda: entry.insert(END, six['text'])) 
	six.grid(row = 3, column = 2)
	seven = Button(root, text = '7', width = 10, command = lambda: entry.insert(END, seven['text'])) 
	seven.grid(row = 2, column = 0)
	eigth = Button(root, text = '8', width = 10, command = lambda: entry.insert(END, eigth['text'])) 
	eigth.grid(row = 2, column = 1)
	nine = Button(root, text = '9', width = 10, command = lambda: entry.insert(END, nine['text'])) 
	nine.grid(row = 2, column = 2)
	zero = Button(root, text = '0', width = 21, command = lambda: entry.insert(END, zero['text'])) 
	zero.grid(row = 5, column = 0, columnspan = 2)
	point = Button(root, text = '.', width = 10, command = lambda: entry.insert(END, point['text']))
	point.grid(row = 5, column = 2)


	root.mainloop()

if __name__ == "__main__":
	calculator()
