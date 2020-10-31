from tkinter import *
import operator

root = Tk()
root.title('Calculator')
ops = {'•': operator.mul, '/': operator.truediv,
       '+': operator.add, '_': operator.sub}
expressions = ['/', '•', '_', '+']


e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def MD(type, rawS):
    entered = rawS
    while type in entered:
        for i in range(len(entered)):
            try:
                if entered[i] == type:
                    expressionsL = [0]
                    expressionsR = []
                    for exp in expressions:
                        if entered.rfind(exp, 0, i) != -1:
                            expressionsL.append(entered.rfind(exp, 0, i))
                        if entered.find(exp, i+1) != -1:
                            expressionsR.append(entered.find(exp, i+1))
                    closeL = max(expressionsL)
                    if closeL == 0:
                        if expressionsR:
                            closeR = (min(expressionsR))
                            middle = str(
                                '%.2f' % (ops[type](float(entered[closeL:i]), float(entered[i+1:closeR]))))
                            entered = (middle+entered[closeR:])
                        else:
                            middle = str(
                                '%.2f' % (ops[type](float(entered[closeL:i]), float(entered[i+1:]))))
                            entered = (middle)
                    elif expressionsR:
                        closeR = (min(expressionsR))
                        middle = str(
                            '%.2f' % (ops[type](float(entered[closeL+1:i]), float(entered[i+1:closeR]))))
                        entered = (entered[:closeL+1]+middle+entered[closeR:])
                    else:
                        middle = str(
                            '%.2f' % (ops[type](float(entered[closeL+1:i]), float(entered[i+1:]))))
                        entered = (entered[:closeL+1]+middle)
            except:
                pass
    return entered


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_equal():
    final = e.get()
    final = final.replace('-', '_')
    for exp in expressions:
        final = (MD(exp, final))
    e.delete(0, END)
    e.insert(0, final)


# Define Buttons
button_1 = Button(root, text='1', padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20,
                  command=lambda: button_click(0))

button_add = Button(root, text='+', padx=40, pady=20,
                    command=lambda: button_click('+'))
button_subtract = Button(root, text='-', padx=41, pady=20,
                         command=lambda: button_click('-'))
button_divide = Button(root, text='/', padx=41, pady=20,
                       command=lambda: button_click('/'))
button_mult = Button(root, text='*', padx=41, pady=20,
                     command=lambda: button_click('•'))
button_clear = Button(root, text='Clear', padx=27.4,
                      pady=20, command=button_clear)
button_equal = Button(root, text='=', padx=127.5,
                      pady=20, command=button_equal)

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_add.grid(row=4, column=2)


button_mult.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_subtract.grid(row=5, column=2)

button_equal.grid(row=6, column=0, columnspan=3)
button_clear.grid(row=4, column=0)

root.mainloop()
