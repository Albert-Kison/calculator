from tkinter import *


def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def erase_button_pressed(display):
    display.set("")


def equal_button_pressed(display):
    display.set(evaluate(display.get()))


def evaluate(string):

    # validate string
    string = string.replace(" ", "")

    for ch in string:
        if ch not in "0123456789.+-/*":
            return "error"

    for ch in "+-*/":
        if string.startswith(ch) or string.endswith(ch):
            return "error"


    def split_by(string, sep):
        lis = []
        current = ""
        for ch in string:
            if ch in sep:
                lis.append(current)
                lis.append(ch)
                current = ""
            else:
                current += ch

        lis.append(current)

        return lis


    def do_operations(lis):
        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = float(lis[1])
            lis = lis[2:]

            if operator == "+":
                output += number
            elif operator == "-":
                output -= number
            elif operator == "*":
                output *= number
            elif operator == "/":
                output /= number

        return output


    lis = split_by(string, "+-")

    # multiplication and division first
    for i in range(len(lis)):
        el = lis[i]
        if '*' in el or '/' in el:
            lis[i] = do_operations(split_by(el, "*/"))

    # addition and subtraction
    return do_operations(lis)


app = Tk()

# setting up the UI
display = StringVar()
Entry(app, relief=RIDGE, textvariable=display, justify='right', bg="green", foreground='white').pack(side=TOP, expand=YES, fill=BOTH)

EraseButton = iCalc(app, TOP)
button(EraseButton, LEFT, 'C', lambda: erase_button_pressed(display))

for numButton in ("789/", "456*", "123-", "0.+"):
    FunctionNum = iCalc(app, TOP)
    for ch in numButton:
        button(FunctionNum, LEFT, ch, lambda display=display, ch=ch: display.set(display.get() + ch))

EqualButton = iCalc(app, TOP)
button(EqualButton, LEFT, '=', lambda: equal_button_pressed(display))

app.mainloop()
