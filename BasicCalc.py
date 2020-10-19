'''
Author: Hrishikesh Naramparambath
Basic Calc v1.0
Advanced features comming soon!
'''

import tkinter as tk
import tkmacosx as tkmac
import numpy as np
import math
import pandas as pd
import cmath as cm

'''import tempfile
import pathlib
import platform'''

expression = ''

root = tk.Tk()
root.title("BasicCalc")
root.resizable(0,0)
root.configure(bg = '#1F2739')

global max_index
max_index = 0

global cur_index
cur_index = 0


'''global tempdir
tempdir = pathlib.Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())'''


Entry1 = tk.Entry(width=20, bg='#1F2739', fg='white', borderwidth=0, justify='right', font='Comfortaa 32', highlightbackground='#1F2739')
Entry1.grid(row = 0, columnspan = 7)
Entry1.insert(0, '0')

operation_list = ['+','-','*','/']

#Defining functions for calc  

#Addition
def add():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    if expression in ('','0'):
        pass
    elif expression in operation_list:
        Entry1.delete(0, 'end')
    elif expression[-1] in operation_list:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '+')
    else:
        Entry1.insert('end','+')

#Subtraction
def subtract():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    if expression == '':
        Entry1.insert('end', '-')
    elif expression == '0':
        Entry1.delete(0, 'end')
        Entry1.insert('end', '-')
    elif expression[-1] in operation_list:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '-')
    else:
        Entry1.insert('end','-')

#Multiplication
def multiply():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    if expression in ('','0'):
        pass
    elif expression in operation_list:
        Entry1.delete(0, 'end')
    elif expression[-1] in operation_list:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '*')
    else:
        Entry1.insert('end','*')

#Division
def divide():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    if expression in ('','0'):
        pass
    elif expression in operation_list:
        Entry1.delete(0, 'end')
    elif expression[-1] in operation_list:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '/')
    else:
        Entry1.insert('end','/')


error_list_for_reciprocal = ['Syntax Error', 'Error: Division by Zero', 'Error: Empty Memory', 'undefined']

#Reciprocal Button

def reciprocal():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    if expression == '0':
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'undefined')
    try:
        if expression in error_list_for_reciprocal:
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Syntax Error')
        elif expression == '0':
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Error: Division by Zero')
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, 1/eval(expression))
    except:
        if expression != '0':
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Syntax Error')
    Entry1.config(state = tk.DISABLED, disabledbackground='#1F2739', disabledforeground='white')

#Square

def square():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    try:
        if expression in error_list_for_reciprocal:
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Syntax Error')
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, (eval(expression))**2)
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'Syntax Error')
    Entry1.config(state = tk.DISABLED, disabledbackground='#1F2739', disabledforeground='white')

#SQRT

def square_root():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    try:
        if expression in error_list_for_reciprocal:
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Syntax Error')
        elif eval(expression) >= 0:
            Entry1.delete(0, 'end')
            Entry1.insert(0, math.sqrt((eval(expression))))
        elif eval(expression) < 0:
            Entry1.delete(0, 'end')
            Entry1.insert(0, cm.sqrt((eval(expression))))
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'Syntax Error')
    Entry1.config(state = tk.DISABLED, disabledbackground='#1F2739', disabledforeground='white')

#Natural Log

def natural_log():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    try:
        if expression in error_list_for_reciprocal:
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Syntax Error')
        elif eval(expression) > 0:
            Entry1.delete(0, 'end')
            Entry1.insert(0, math.log(eval(expression)))
        elif eval(expression) <= 0:
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'undefined')
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'Syntax Error')
    Entry1.config(state = tk.DISABLED, disabledbackground='#1F2739', disabledforeground='white')

y = []
#Equal To Sign
def equal_to():
    global expression
    global Entry1
    global max_index
    global cur_index
    global database
    global y
    
    expression = str(Entry1.get())
    database = pd.DataFrame()
    
    try:
        if '/0' not in expression:
            y = y + [expression]
            database['History'] = y
            print(database)
            database.to_csv(r'Calculations_History.csv')
            Entry1.delete(0, 'end')
            Entry1.insert(0, eval(expression))
            
        elif '/0' in expression:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Error: Division by Zero")
        max_index = max_index + 1
        cur_index = max_index
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'Syntax Error')
    
    Entry1.config(state = tk.DISABLED, disabledbackground='#1F2739', disabledforeground='white')

#History Recalling
def history_reverse(event):
    global import_database
    global cur_index
    Entry1.config(state=tk.NORMAL)
    import_database = pd.read_csv(r'Calculations_History.csv')
    if cur_index > 0:
        Entry1.delete(0, 'end')
        Entry1.insert(0, import_database.at[cur_index - 1, 'History'])
        cur_index = cur_index - 1
    else:
        Entry1.delete(0, 'end')
        Entry1.insert(0, import_database.at[0, 'History'])

def history_forward(event):
    global import_database
    global cur_index
    Entry1.config(state=tk.NORMAL)
    import_database = pd.read_csv(r'Calculations_History.csv')
    if cur_index < len(import_database) - 1:
        Entry1.delete(0, 'end')
        Entry1.insert(0, import_database.at[cur_index + 1, 'History'])
        cur_index = cur_index + 1
    else:
        Entry1.delete(0, 'end')
        Entry1.insert(0, import_database.at[cur_index, 'History'])
    

    
    
#Clear Button
def clear():
    Entry1.config(state = tk.NORMAL)
    Entry1.delete(0, 'end')
    Entry1.insert(0, '0')

#Delete Button
def delete():
    global expression
    expression = str(Entry1.get())
    if Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
    else:
        Entry1.delete(0, 'end')
        Entry1.insert(0, expression[:-1])


#Memory ADD

def memory_add():
    global memorylist
    global expression
    Entry1.config(state = tk.NORMAL)
    expression = str(Entry1.get())
    memorylist = []

    try:
        memorylist = memorylist + [eval(expression)]
        Entry1.delete(0, 'end')
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'Syntax Error')
    
 
#Recall from Memory
def memory_recall():
    global memorylist
    global expression
    expression = str(Entry1.get())
    if expression.isnumeric() == False:
        Entry1.insert('end', memorylist[0])
    else:
        Entry1.delete(0, 'end')
        Entry1.insert('end', memorylist[0])


    
#Percentage
def percentage():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    try:
        if '/0' in expression:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Error: Division By Zero")
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, eval(expression)*100)
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, "Syntax Error")


error_list_for_trig = ['', 'Syntax Error', 'Error: Division By Zero', 'undefined', 'Error: Empty Memory']

#Sine function

def sine_function():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    try:
        if expression in error_list_for_trig:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Syntax Error")
        elif expression == '3.141592653589793':
            Entry1.delete(0, 'end')
            Entry1.insert(0, '0')
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, np.sin(eval(expression)))
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, "Syntax Error")
    Entry1.config(state = tk.DISABLED, disabledbackground='#1F2739', disabledforeground='white')
        
#Cos function
def cos_function():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    try:
        if expression in error_list_for_trig:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Syntax Error")
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, np.cos(eval(expression)))
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, "Syntax Error")
    Entry1.config(state = tk.DISABLED, disabledbackground='#1F2739', disabledforeground='white')

#Tan function
def tan_function():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state = tk.NORMAL)
    try:
        if expression in error_list_for_trig:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Syntax Error")
        elif expression == '3.141592653589793':
            Entry1.delete(0, 'end')
            Entry1.insert(0, '0')
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, np.tan(eval(expression)))
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, "Syntax Error")
    Entry1.config(state = tk.DISABLED, disabledbackground='#1F2739', disabledforeground='white')

error_list_for_constant = ['0', 'Syntax Error', 'Error: Division By Zero', 'undefined', 'Error: Empty Memory']

#Pi constant
def pi_constant():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_constant:
        Entry1.delete(0, 'end')
        Entry1.insert('end', np.pi)
    elif expression[-1] not in operation_list:
        Entry1.delete(0, 'end')
        Entry1.insert('end', np.pi)
    else:
        Entry1.insert('end', np.pi)

#e constant
def e_constant():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_constant:
        Entry1.delete(0, 'end')
        Entry1.insert('end', np.e)
    elif expression[-1] not in operation_list:
        Entry1.delete(0, 'end')
        Entry1.insert('end', np.e)
    else:
        Entry1.insert('end', np.e)

error_list_for_numbers = ['0', 'Syntax Error', 'Error: Division By Zero', 'undefined', 'Error: Empty Memory']

#Numbers Buttons
def button1_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button1.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button1.cget('text'))
    else:
        Entry1.insert('end',Button1.cget('text'))
        
def button2_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button2.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button2.cget('text'))
    else:
        Entry1.insert('end',Button2.cget('text'))

def button3_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button3.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button3.cget('text'))
    else:
        Entry1.insert('end',Button3.cget('text'))
        
def button4_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button4.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button4.cget('text'))
    else:
        Entry1.insert('end',Button4.cget('text'))
        
def button5_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button5.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button5.cget('text'))
    else:
        Entry1.insert('end',Button5.cget('text'))
        
def button6_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button6.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button6.cget('text'))
    else:
        Entry1.insert('end',Button6.cget('text'))
        
def button7_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button7.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button7.cget('text'))
    else:
        Entry1.insert('end',Button7.cget('text'))
        
def button8_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button8.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button8.cget('text'))
    else:
        Entry1.insert('end',Button8.cget('text'))
        
def button9_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button9.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button9.cget('text'))
    else:
        Entry1.insert('end',Button9.cget('text'))
        
def button0_click():
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button0.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state = tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end',Button0.cget('text'))
    else:
        Entry1.insert('end',Button0.cget('text'))

#Decimal Button
def decimal():
    Entry1.insert('end',Button_Decimal.cget('text'))


#User Interface - Buttons

#Numbers

Button1 = tkmac.Button(root, text = "1", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button1_click)
Button1.grid(column = 3, row = 4)

Button2 = tkmac.Button(root, text = "2", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button2_click)
Button2.grid(column = 4, row = 4)

Button3 = tkmac.Button(root, text = "3", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button3_click)
Button3.grid(column = 5, row = 4)

Button4 = tkmac.Button(root, text = "4", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button4_click)
Button4.grid(column = 3, row = 3)

Button5 = tkmac.Button(root, text = "5", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button5_click)
Button5.grid(column = 4, row = 3)

Button6 = tkmac.Button(root, text = "6", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button6_click)
Button6.grid(column = 5, row = 3)

Button7 = tkmac.Button(root, text = "7", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button7_click)
Button7.grid(column = 3, row = 2)

Button8 = tkmac.Button(root, text = "8", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button8_click)
Button8.grid(column = 4, row = 2)

Button9 = tkmac.Button(root, text = "9", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button9_click)
Button9.grid(column = 5, row = 2)

Button0 = tkmac.Button(root, text = "0", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=button0_click)
Button0.grid(column = 4, row = 5)

#Special constants

pi_button = tkmac.Button(root, text = "π", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=pi_constant)
pi_button.grid(column = 2, row = 5)

e_button = tkmac.Button(root, text = "e", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=e_constant)
e_button.grid(column = 1, row = 5)

#Decimal Point

Button_Decimal = tkmac.Button(root, text = ".", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=decimal)
Button_Decimal.grid(column = 3, row = 5)


#Operations
add_button = tkmac.Button(root, text = "+", height=80, width=80, bg='orange', activebackground='#FFAE00', activeforeground='black', command=add)
add_button.grid(column = 6, row = 1)

subtract_button = tkmac.Button(root, text = "-", height=80, width=80, bg='orange', activebackground='#FFAE00', activeforeground='black', command=subtract)
subtract_button.grid(column = 6, row = 2)

multiply_button = tkmac.Button(root, text = "x", height=80, width=80, bg='orange', activebackground='#FFAE00', activeforeground='black', command=multiply)
multiply_button.grid(column = 6, row = 3)

divide_button = tkmac.Button(root, text = "÷", height=80, width=80, bg='orange', activebackground='#FFAE00', activeforeground='black', command=divide)
divide_button.grid(column = 6, row = 4)

equal_button = tkmac.Button(root, text = "=", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=equal_to)
equal_button.grid(column = 5, row = 5)

percentage_button = tkmac.Button(root, text = "%", height=80, width=80, bg='orange', activebackground='#FFAE00', activeforeground='black', command=percentage)
percentage_button.grid(column = 6, row = 5)

#Clear

clear_button = tkmac.Button(root, text = "CLR", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=clear)
clear_button.grid(column = 2, row = 1)

#Delete

delete_button = tkmac.Button(root, text = '⇦', height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=delete)
delete_button.grid(column = 5, row = 1)

#Memory

memory_add = tkmac.Button(root, text = "M+", height=80, width=80,  bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=memory_add)
memory_add.grid(column = 3, row = 1)

memory_recall = tkmac.Button(root, text = "MR", height=80, width=80,  bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=memory_recall)
memory_recall.grid(column = 4, row = 1)

#Trigonometric functions

sin_button = tkmac.Button(root, text = "sin", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=sine_function)
sin_button.grid(column = 2, row = 2)

cos_button = tkmac.Button(root, text = "cos", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=cos_function)
cos_button.grid(column = 2, row = 3)

tan_button = tkmac.Button(root, text = "tan", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=tan_function)
tan_button.grid(column = 2, row = 4)


#Additional Math Functions

reciprocal_button = tkmac.Button(root, text = "1/x", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=reciprocal)
reciprocal_button.grid(column = 1, row = 1)

square_button = tkmac.Button(root, text = "x²", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=square)
square_button.grid(column = 1, row = 2)

sqrt_button = tkmac.Button(root, text = "√x", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=square_root)
sqrt_button.grid(column = 1, row = 3)

naturallog_button = tkmac.Button(root, text = "ln", height=80, width=80, bg='#1F2739', fg='white', activebackground='#171A2F', activeforeground='white', command=natural_log)
naturallog_button.grid(column = 1, row = 4)





root.bind('<Up>', history_reverse)
root.bind('<Down>', history_forward)


root.mainloop()
