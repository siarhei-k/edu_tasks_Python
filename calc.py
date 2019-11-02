from tkinter import *
from tkinter.messagebox import *
from random import *


def themes(t):
    if t == 1:
        win.config(bg='lightgray')
        for i in buttons:
            i.config(fg='black', bg='white')
        win.title('Калькулятор. Светлый')
    elif t == 2:
        win.config(bg='darkgray')
        for i in buttons:
            i.config(fg='white', bg='dimgray')
        win.title('Калькулятор. Темный')
    elif t == 3:
        color_random = choice(colors)
        win.config(bg='firebrick')
        win.title('Калькулятор. Цветной')
        for d in range(0, 8):
            buttons[d].config(fg='yellow', bg=color_random)
        color_random = choice(colors)
        for d in range(8, 16):
            buttons[d].config(fg='yellow', bg=color_random)
        color_random = choice(colors)
        for d in range(16, 23):
            buttons[d].config(fg='yellow', bg=color_random)
        #for i in buttons:
           # i.config(fg='yellow', bg=color_random)

def setting():
    win2 = Tk()
    win2.title('Найстройки')
    win2.geometry('300x150'+'+600+100')

    Label(win2, text='Темы').grid(row=0, column=0)

    t = IntVar()
    cmd = lambda x=1: themes(x)
    r1 = Radiobutton(win2, text='Светлая', variable=t, value=1, command=cmd)
    r1.grid(row=1, column=0, sticky=W)
    r1.select()

    cmd = lambda x=2: themes(x)
    r2 = Radiobutton(win2, text='Темная', variable=t, value=2, command=cmd)
    r2.grid(row=2, column=0, sticky=W)

    cmd = lambda x=3: themes(x)
    r3 = Radiobutton(win2, text='Цветная', variable=t, value=3, command=cmd)
    r3.grid(row=3, column=0, sticky=W)

def counter(key):
    if key in '0123456789+-*/.()':
        entry.insert(END, key)
    else:
        if key == '√':
            entry.insert(END, '**(0.5)')
        else:
            if key == 'x²':
                entry.insert(END, '**(2)')
            else:
                if key == 'x³':
                    entry.insert(END, '**(3)')
                else:
                    if key == '=':
                        try:
                            result = eval(entry.get())
                            entry.insert(END, '=' + str(result))
                        except SyntaxError:
                            showerror('Ошибка', 'Ошибка в синтаксисе')
                        except ZeroDivisionError:
                            showerror('Ошибка', 'Деление на ноль')
                        except NameError:
                            showerror('Ошибка', 'Некорректный ввод')
                    else:
                        if key == 'C':
                            entry.delete(0, END)
                        else:
                            if key == '←':
                                entry.delete(len(entry.get())-1)



def about():
    showinfo("О программе", 'Было долго. Но я сделал это')

win = Tk()
win.title('Калькулятор')
win.resizable(width=False, height=False)

m = Menu(win)
win.config(menu=m)

item1 = Menu(m, tearoff=0)
m.add_cascade(label='Справка', menu=item1)
item1.add_command(label='О программе', command=about)

m.add_command(label='Настройка', command=setting)

entry = Entry(width=60, bd=3, relief=SUNKEN)
entry.grid(row=0, columnspan=8)

colors = ['red', 'green', 'blue', 'gray', 'black']

buttons_all = ['7', '8', '9', '0', '+', '-', '*', '/',
               '4', '5', '6', 'x²', 'x³', '√', '(', ')',
               '1', '2', '3', '.', '←', 'C', '=', '',
              ]

buttons = []

c = 0
r = 1
for i in buttons_all:
    cmd = lambda x=i: counter(x)
    btn = Button(win, text=i, width=8, bd=4, command=cmd, font=('bold'))
    btn.grid(row=r, column=c, padx=1, pady=1)
    buttons.append(btn)
    c += 1
    if c > 7:
        c = 0
        r += 1

win.mainloop()
