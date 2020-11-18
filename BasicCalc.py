"""
Author: Hrishikesh Naramparambath
SciCalc
"""

# Importing modules

import tkinter as tk
from tkmacosx import Button
import numpy as np
import math
import pandas as pd
import cmath as cm
import platform

# Main Window
root = tk.Tk()
root.title("BasicCalc")
root.resizable(0, 0)
root.configure(bg='#1B2131')

# Variables

global max_index
max_index = 0

global cur_index
cur_index = 0

expression = ''

# Cross-platform feature
if platform.system() == 'Darwin':
    Entry1 = tk.Entry(width=20, bg='#1B2131', fg='white', borderwidth=0, justify='right', font='Arial 41 bold',
                      highlightbackground='#1B2131')
    Entry1.grid(row=0, columnspan=7)
    Entry1.insert(0, '0')

else:
    Entry1 = tk.Entry(width=20, bg='#1B2131', fg='white', borderwidth=0, justify='right', font='Arial 32 bold',
                      highlightbackground='#1B2131')
    Entry1.grid(row=0, columnspan=7)
    Entry1.insert(0, '0')

# Operations List
operation_list = ['+', '-', '×', '÷', '^']

# Lists of Errors
error_list = ['Syntax Error', 'Error: Division by Zero', 'Error: Empty Memory', 'undefined']
error_list_for_reciprocal = error_list
error_list_for_trig = [''] + error_list
error_list_for_constant = ['0'] + error_list
error_list_for_numbers = error_list_for_constant

# Defining Functions

'''
Arithmetic Operations
Addition, Subtraction, Multiplication and Division
'''


# Addition
def add():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if expression in ('', '0'):
        pass
    elif expression in operation_list:
        Entry1.delete(0, 'end')
    elif expression[-1] in operation_list:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '+')
    else:
        Entry1.insert('end', '+')


# Subtraction
def subtract():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if expression == '':
        Entry1.insert('end', '-')
    elif expression == '0':
        Entry1.delete(0, 'end')
        Entry1.insert('end', '-')
    elif expression[-1] in ['+', '-', '×', '÷']:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '-')
    elif expression[-1] == '^':
        Entry1.insert('end', '-')
    else:
        Entry1.insert('end', '-')

    # Multiplication


def multiply():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if expression in ('', '0'):
        pass
    elif expression in operation_list:
        Entry1.delete(0, 'end')
    elif expression[-1] in operation_list:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '×')
    else:
        Entry1.insert('end', '×')


# Division
def divide():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if expression in ('', '0'):
        pass
    elif expression in operation_list:
        Entry1.delete(0, 'end')
    elif expression[-1] in operation_list:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '÷')
    else:
        Entry1.insert('end', '÷')


'''
Mathematical functions
Reciprocal, square, sqrt, natural logarithm
'''


# Reciprocal Button
def reciprocal():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if expression == '0':
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'undefined')
    elif '×' or '÷' or '^' or 'π' or 'e' in expression:
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(np.pi))
        expression = expression.replace('e', str(np.e))
    try:
        if expression in error_list_for_reciprocal:
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Syntax Error')
        elif expression == '0':
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Error: Division by Zero')
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, round((1 / eval(expression)), 5))
    except:
        if expression != '0':
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Syntax Error')
    Entry1.config(state=tk.DISABLED, disabledbackground='#1B2131', disabledforeground='white')


# Power
def power():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if expression in (''):
        pass
    elif expression in operation_list:
        Entry1.delete(0, 'end')
    elif expression[-1] in operation_list:
        Entry1.delete(0, 'end')
        expression = expression[:-1]
        Entry1.insert(0, expression)
        Entry1.insert('end', '^')
    else:
        Entry1.insert('end', '^')


# SQRT

def square_root():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if '×' or '÷' or '^' or 'π' or 'e' in expression:
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(np.pi))
        expression = expression.replace('e', str(np.e))
    try:
        if expression in error_list_for_reciprocal:
            Entry1.delete(0, 'end')
            Entry1.insert(0, 'Syntax Error')
        elif eval(expression) >= 0:
            Entry1.delete(0, 'end')
            Entry1.insert(0, round(math.sqrt((eval(expression))), 5))
        elif eval(expression) < 0:
            Entry1.delete(0, 'end')
            Entry1.insert(0, cm.sqrt(eval(expression)))
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'Syntax Error')
    Entry1.config(state=tk.DISABLED, disabledbackground='#1B2131', disabledforeground='white')


# Natural Log

def natural_log():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if '×' or '÷' or '^' or 'π' or 'e' in expression:
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(np.pi))
        expression = expression.replace('e', str(np.e))
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
    Entry1.config(state=tk.DISABLED, disabledbackground='#1B2131', disabledforeground='white')


# Miscellaneous
# Equal To Sign
y = []


def equal_to(*args):
    global expression
    global Entry1
    global max_index
    global cur_index
    global database
    global y

    expression = str(Entry1.get())
    database = pd.DataFrame()

    try:
        if expression[-2:] != '÷0':
            if '×' or '÷' or '^' or 'π' in expression:
                y = y + [expression]
                database['History'] = y
                print(database)
                expression = expression.replace('×', '*')
                expression = expression.replace('÷', '/')
                expression = expression.replace('^', '**')
                expression = expression.replace('π', str(np.pi))
                database.to_csv(r'Calculations_History.csv')
                Entry1.delete(0, 'end')
                Entry1.insert(0, eval(expression))

            elif 'e' in expression:
                expression.index['e'] = x
                if eval(expression[x - 1]).isnumeric() == True and expression[x + 1] in ['+', '-']:
                    pass
                else:
                    expression = expression.replace('e', str(np.e))

            else:
                y = y + [expression]
                database['History'] = y
                print(database)
                database.to_csv(r'Calculations_History.csv')
                Entry1.delete(0, 'end')
                Entry1.insert(0, eval(expression))

        elif expression[-2:] == '÷0':
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Error: Division by Zero")

        max_index = max_index + 1
        cur_index = max_index
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'Syntax Error')
    if str(Entry1.get()) != '0':
        Entry1.config(state=tk.DISABLED, disabledbackground='#1B2131', disabledforeground='white')
    else:
        pass


# Clear Button
def clear():
    Entry1.config(state=tk.NORMAL)
    Entry1.delete(0, 'end')
    Entry1.insert(0, '0')


# Delete Button
def delete(*args):
    global expression
    expression = str(Entry1.get())
    if Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
    elif len(expression) == 1:
        Entry1.delete(0, 'end')
        Entry1.insert(0, '0')
    else:
        Entry1.delete(0, 'end')
        Entry1.insert(0, expression[:-1])


# Percentage
def percentage():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if '×' or '÷' or '^' or 'π' or 'e' in expression:
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(np.pi))
        expression = expression.replace('e', str(np.e))
    try:
        if '÷0' in expression:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Error: Division By Zero")
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, eval(expression) * 100)
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, "Syntax Error")


# Decimal Button
def decimal():
    global expression
    expression = str(Entry1.get())
    if expression[-1] in operation_list:
        Entry1.insert('end', '0.')
    else:
        Entry1.insert('end', '.')


'''
Advanced features
History and Memory
'''


# History Recalling
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
    global expression
    Entry1.config(state=tk.NORMAL)
    import_database = pd.read_csv(r'Calculations_History.csv')
    expression = str(Entry1.get())
    try:
        if cur_index < len(import_database) - 1:
            Entry1.delete(0, 'end')
            Entry1.insert(0, import_database.at[cur_index + 1, 'History'])
            cur_index = cur_index + 1
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, import_database.at[cur_index, 'History'])
    except KeyError:
        Entry1.delete(0, 'end')
        Entry1.insert(0, expression)


# Memory ADD
def memory_add():
    global memory
    global expression
    Entry1.config(state=tk.NORMAL)
    expression = str(Entry1.get())
    if '×' or '÷' or '^' or 'π' or 'e' in expression:
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(np.pi))
        expression = expression.replace('e', str(np.e))
    try:
        if expression not in ('', '0'):
            memory = str(eval(expression))
            Entry1.delete(0, 'end')
            Entry1.insert('end', '0')
        else:
            pass
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, 'Syntax Error')


# Recall from Memory
def memory_recall():
    global memory
    global expression
    expression = str(Entry1.get())

    try:
        if expression.isnumeric() == False:
            memory = memory.replace(str(np.e), 'e')
            memory = memory.replace(str(np.pi), 'π')
            Entry1.insert('end', memory)
        else:
            memory = memory.replace(str(np.e), 'e')
            memory = memory.replace(str(np.pi), 'π')
            Entry1.delete(0, 'end')
            Entry1.insert('end', memory)
    except:
        Entry1.insert('end', '')


'''
Trigonometric Functions
sine, cosine, tangent
'''


# Sine function
def sine_function():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if '×' or '÷' or '^' or 'π' or 'e' in expression:
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(np.pi))
        expression = expression.replace('e', str(np.e))
    try:
        if expression in error_list_for_trig:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Syntax Error")
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, round(np.sin(eval(expression)), 5))
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, "Syntax Error")
    Entry1.config(state=tk.DISABLED, disabledbackground='#1B2131', disabledforeground='white')


# Cos function
def cos_function():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if '×' or '÷' or '^' or 'π' or 'e' in expression:
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(np.pi))
        expression = expression.replace('e', str(np.e))
    try:
        if expression in error_list_for_trig:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Syntax Error")
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, round(np.cos(eval(expression)), 5))
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, "Syntax Error")
    Entry1.config(state=tk.DISABLED, disabledbackground='#1B2131', disabledforeground='white')


# Tan function
def tan_function():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)
    if '×' or '÷' or '^' or 'π' or 'e' in expression:
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(np.pi))
        expression = expression.replace('e', str(np.e))
    try:
        if expression in error_list_for_trig:
            Entry1.delete(0, 'end')
            Entry1.insert(0, "Syntax Error")
        else:
            Entry1.delete(0, 'end')
            Entry1.insert(0, round(np.tan(eval(expression)), 5))
    except:
        Entry1.delete(0, 'end')
        Entry1.insert(0, "Syntax Error")
    Entry1.config(state=tk.DISABLED, disabledbackground='#1B2131', disabledforeground='white')


'''
Special constants
pi and Euler's number
'''


# Pi constant
def pi_constant():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)

    if expression in error_list_for_constant:
        Entry1.delete(0, 'end')
        Entry1.insert('end', 'π')
    elif expression[-1] not in operation_list:
        Entry1.delete(0, 'end')
        Entry1.insert('end', 'π')
    else:
        Entry1.insert('end', 'π')


# e constant
def e_constant():
    global expression
    expression = str(Entry1.get())
    Entry1.config(state=tk.NORMAL)

    if expression in error_list_for_constant:
        Entry1.delete(0, 'end')
        Entry1.insert('end', 'e')
    elif expression[-1] not in operation_list:
        Entry1.delete(0, 'end')
        Entry1.insert('end', 'e')
    else:
        Entry1.insert('end', 'e')


'''
Numerals/Digits
'''


# Numbers Buttons
def button1_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button1.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button1.cget('text'))
    else:
        Entry1.insert('end', Button1.cget('text'))


def button2_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button2.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button2.cget('text'))
    else:
        Entry1.insert('end', Button2.cget('text'))


def button3_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button3.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button3.cget('text'))
    else:
        Entry1.insert('end', Button3.cget('text'))


def button4_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button4.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button4.cget('text'))
    else:
        Entry1.insert('end', Button4.cget('text'))


def button5_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button5.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button5.cget('text'))
    else:
        Entry1.insert('end', Button5.cget('text'))


def button6_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button6.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button6.cget('text'))
    else:
        Entry1.insert('end', Button6.cget('text'))


def button7_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button7.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button7.cget('text'))
    else:
        Entry1.insert('end', Button7.cget('text'))


def button8_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button8.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button8.cget('text'))
    else:
        Entry1.insert('end', Button8.cget('text'))


def button9_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button9.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button9.cget('text'))
    else:
        Entry1.insert('end', Button9.cget('text'))


def button0_click(*args):
    global expression
    expression = str(Entry1.get())
    if expression in error_list_for_numbers:
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button0.cget('text'))
    elif Entry1.cget('state') == tk.DISABLED:
        Entry1.config(state=tk.NORMAL)
        Entry1.delete(0, 'end')
        Entry1.insert('end', Button0.cget('text'))
    else:
        Entry1.insert('end', Button0.cget('text'))


'''
User Interface
'''

# Numbers

Button1 = Button(root, font='Helvetica 14', text="1", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button1_click)
Button1.grid(column=3, row=4)

Button2 = Button(root, font='Helvetica 14', text="2", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button2_click)
Button2.grid(column=4, row=4)

Button3 = Button(root, font='Helvetica 14', text="3", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button3_click)
Button3.grid(column=5, row=4)

Button4 = Button(root, font='Helvetica 14', text="4", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button4_click)
Button4.grid(column=3, row=3)

Button5 = Button(root, font='Helvetica 14', text="5", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button5_click)
Button5.grid(column=4, row=3)

Button6 = Button(root, font='Helvetica 14', text="6", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button6_click)
Button6.grid(column=5, row=3)

Button7 = Button(root, font='Helvetica 14', text="7", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button7_click)
Button7.grid(column=3, row=2)

Button8 = Button(root, font='Helvetica 14', text="8", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button8_click)
Button8.grid(column=4, row=2)

Button9 = Button(root, font='Helvetica 14', text="9", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button9_click)
Button9.grid(column=5, row=2)

Button0 = Button(root, font='Helvetica 14', text="0", height=80, width=80, bg='#1B2131', fg='white',
                 activebackground='#171A2F', activeforeground='white', command=button0_click)
Button0.grid(column=4, row=5)

# Special constants

pi_button = Button(root, font='Helvetica 14', text="π", height=80, width=80, bg='#1B2131', fg='white',
                   activebackground='#171A2F', activeforeground='white', command=pi_constant)
pi_button.grid(column=2, row=5)

e_button = Button(root, font='Helvetica 14', text="e", height=80, width=80, bg='#1B2131', fg='white',
                  activebackground='#171A2F', activeforeground='white', command=e_constant)
e_button.grid(column=1, row=5)

# Decimal Point

Button_Decimal = Button(root, font='Helvetica 14', text=".", height=80, width=80, bg='#1B2131', fg='white',
                        activebackground='#171A2F', activeforeground='white', command=decimal)
Button_Decimal.grid(column=3, row=5)

# Operations
add_button = Button(root, font='Helvetica 15', text="+", height=80, width=80, bg='orange', activebackground='#FFAE00',
                    activeforeground='black', command=add)
add_button.grid(column=6, row=1)

subtract_button = Button(root, font='Helvetica', text="–", height=80, width=80, bg='orange', activebackground='#FFAE00',
                         activeforeground='black', command=subtract)
subtract_button.grid(column=6, row=2)

multiply_button = Button(root, font='Helvetica', text="×", height=80, width=80, bg='orange', activebackground='#FFAE00',
                         activeforeground='black', command=multiply)
multiply_button.grid(column=6, row=3)

divide_button = Button(root, font='Helvetica 16', text="÷", height=80, width=80, bg='orange',
                       activebackground='#FFAE00', activeforeground='black', command=divide)
divide_button.grid(column=6, row=4)

equal_button = Button(root, font='Helvetica 14', text="=", height=80, width=80, bg='#1B2131', fg='white',
                      activebackground='#171A2F', activeforeground='white', command=equal_to)
equal_button.grid(column=5, row=5)

percentage_button = Button(root, font='Helvetica 14', text="%", height=80, width=80, bg='orange',
                           activebackground='#FFAE00', activeforeground='black', command=percentage)
percentage_button.grid(column=6, row=5)

# Clear

clear_button = Button(root, font='Helvetica 14', text="CLR", height=80, width=80, bg='#1B2131', fg='white',
                      activebackground='#171A2F', activeforeground='white', command=clear)
clear_button.grid(column=2, row=1)

# Delete

delete_button = Button(root, font='Helvetica 14', text='⇦', height=80, width=80, bg='#1B2131', fg='white',
                       activebackground='#171A2F', activeforeground='white', command=delete)
delete_button.grid(column=5, row=1)

# Memory

memory_add = Button(root, font='Helvetica 14', text="M+", height=80, width=80, bg='#1B2131', fg='white',
                    activebackground='#171A2F', activeforeground='white', command=memory_add)
memory_add.grid(column=3, row=1)

memory_recall = Button(root, font='Helvetica 14', text="MR", height=80, width=80, bg='#1B2131', fg='white',
                       activebackground='#171A2F', activeforeground='white', command=memory_recall)
memory_recall.grid(column=4, row=1)

# Trigonometric functions

sin_button = Button(root, font='Helvetica 14', text="sin", height=80, width=80, bg='#1B2131', fg='white',
                    activebackground='#171A2F', activeforeground='white', command=sine_function)
sin_button.grid(column=2, row=2)

cos_button = Button(root, font='Helvetica 14', text="cos", height=80, width=80, bg='#1B2131', fg='white',
                    activebackground='#171A2F', activeforeground='white', command=cos_function)
cos_button.grid(column=2, row=3)

tan_button = Button(root, font='Helvetica 14', text="tan", height=80, width=80, bg='#1B2131', fg='white',
                    activebackground='#171A2F', activeforeground='white', command=tan_function)
tan_button.grid(column=2, row=4)

# Additional Math Functions

reciprocal_button = Button(root, font='Helvetica 14', text='1/x', height=80, width=80, bg='#1B2131', fg='white',
                           activebackground='#171A2F', activeforeground='white', command=reciprocal)
reciprocal_button.grid(column=1, row=1)

power_button = Button(root, font='Helvetica 14', text=("x\u02b8"), height=80, width=80, bg='#1B2131', fg='white',
                      activebackground='#171A2F', activeforeground='white', command=power)
power_button.grid(column=1, row=2)

sqrt_button = Button(root, font='Helvetica 14', text="√x", height=80, width=80, bg='#1B2131', fg='white',
                     activebackground='#171A2F', activeforeground='white', command=square_root)
sqrt_button.grid(column=1, row=3)

naturallog_button = Button(root, font='Helvetica 14', text="ln", height=80, width=80, bg='#1B2131', fg='white',
                           activebackground='#171A2F', activeforeground='white', command=natural_log)
naturallog_button.grid(column=1, row=4)

# Binding keys to history functions
root.bind('<Up>', history_reverse)
root.bind('<Down>', history_forward)
root.bind('<Return>', equal_to)
root.bind('<BackSpace>', delete)

root.bind('1', button1_click)
root.bind('2', button2_click)
root.bind('3', button3_click)
root.bind('4', button4_click)
root.bind('5', button5_click)
root.bind('6', button6_click)
root.bind('7', button7_click)
root.bind('8', button8_click)
root.bind('9', button9_click)
root.bind('0', button0_click)


root.mainloop()
