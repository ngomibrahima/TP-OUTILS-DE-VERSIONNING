from tkinter import *
import math as m
root = Tk()
root.title ("Calcuatrice Scientifique Assane ")
e = Entry(root, width = 50, borderwidth = 5, relief = RIDGE, fg = "black", bg = "white")
e.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 15)

# definition de la fonction clique
def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old+to_print)
    return

# definition de la fonction bouton Scientifique
def bs(event):
    key = event.widget
    text = key['text']
    nombre = e.get()
    resultat = ''
    if text == "deg":
        resultat = (m.degrees(float(nombre)))
    if text == "sin":
        resultat = (m.sin(float(nombre)))
    if text == "cos":
        resultat = (m.cos(float(nombre)))
    if text == "tan":
        resultat = (m.tan(float(nombre)))
    if text == "log":
        resultat = (m.log10(float(nombre)))
    if text == "ln":
        resultat = (m.log(float(nombre)))
    if text == "Sqrt":
        resultat = (m.sqrt(float(nombre)))
    if text == "x!":
        resultat = (m.factorial(float(nombre)))
    if text == "1/x":
        resultat = (1/(float(nombre)))
    if text == "pi":
        if nombre == '':
            resultat = (m.pi)
        else:
            resultat = (float(nombre) * m.pi)
    if text == "^":
        if nombre == '':
            resultat = (m.e)
        else:
            resultat = (m.e ** float(nombre))
    e.delete(0, END)
    e.insert(0, resultat)
    

# definition de la fonction effacer
def ac():
    e.delete(0, END)
    return
 
# definition de la fonction backspace
def Bkp():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)

# definition de la fonction evaluer
def evaluer():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)

# creation des boutons
 
lg = Button(root, text = "lg", padx = 28, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
lg.bind("<Button-1>", bs)
ln = Button(root, text = "ln", padx = 28, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
ln.bind("<Button-1>", bs)

par1st = Button(root, text = "(", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black", command= lambda: click("("))
par2nd = Button(root, text = ")", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black", command= lambda: click(")"))
point = Button(root, text = ".", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black", command= lambda: click("."))
exp = Button(root, text = "^s", padx = 23, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
exp.bind("<Button-1>", bs)

degb = Button(root, text = "deg", padx = 23, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
degb.bind("<Button-1>", bs)
sinb = Button(root, text = "sin", padx = 24, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
sinb.bind("<Button-1>", bs)
cosb = Button(root, text = "cos", padx = 23, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
cosb.bind("<Button-1>", bs)
tanb = Button(root, text = "tan", padx = 23, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
tanb.bind("<Button-1>", bs)

sqrtm = Button(root, text = "Sqrt", padx = 23, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
sqrtm.bind("<Button-1>", bs)
eff = Button(root, text = "C", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black", command= lambda: ac())
effTout = Button(root, text = "Bkp", padx = 19, pady = 10, relief = RIDGE, fg = "White", bg = "Black", command= lambda: Bkp())
mod = Button(root, text = "mod", padx = 19, pady = 10, relief = RIDGE, fg = "White", bg = "Black", command= lambda: click("mod"))
div = Button(root, text = "/", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black", command= lambda: click("/"))

fact = Button(root, text = "x!", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
fact.bind("<Button-1>", bs)
sept = Button(root, text = "7", padx = 30, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("7"))
huite = Button(root, text = "8", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("8"))
neuf = Button(root, text = "9", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("9"))
mult = Button(root, text = "*", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("*"))

frac = Button(root, text = "1/x", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
frac.bind("<Button-1>", bs)
quatre = Button(root, text = "4", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("4"))
cinq = Button(root, text = "5", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("5"))
six = Button(root, text = "6", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("6"))
sous = Button(root, text = "-", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("-"))

pib = Button(root, text = "pi", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
pib.bind("<Button-1>", bs)
un = Button(root, text = "1", padx = 30, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("1"))
deux = Button(root, text = "2", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("2"))
trois = Button(root, text = "3", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("3"))
add = Button(root, text = "+", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("+"))

expb = Button(root, text = "e", padx = 29, pady = 10, relief = RIDGE, fg = "White", bg = "Black")
expb.bind("<Button-1>", bs)
zero = Button(root, text = "0", padx = 30, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: click("0"))
egal = Button(root, text = "=", padx = 29, pady = 10, relief = RIDGE, fg = "black", bg = "White", command= lambda: evaluer())

lg.grid(row=1, column=0)
ln.grid(row=1, column=1)
par1st.grid(row=1, column=2)
par2nd.grid(row=1, column=3)
point.grid(row=1, column=4)

exp.grid(row=2, column=0)
degb.grid(row=2, column=1)
sinb.grid(row=2, column=2)
cosb.grid(row=2, column=3)
tanb.grid(row=2, column=4)

sqrtm.grid(row=3, column=0)
eff.grid(row=3, column=1)
effTout.grid(row=3, column=2)
mod.grid(row=3, column=3)
div.grid(row=3, column=4)

fact.grid(row=4, column=0)
sept.grid(row=4, column=1)
huite.grid(row=4, column=2)
neuf.grid(row=4, column=3)
mult.grid(row=4, column=4)

frac.grid(row=5, column=0)
quatre.grid(row=5, column=1)
cinq.grid(row=5, column=2)
six.grid(row=5, column=3)
sous.grid(row=5, column=4)

pib.grid(row=6, column=0)
un.grid(row=6, column=1)
deux.grid(row=6, column=2)
trois.grid(row=6, column=3)
add.grid(row=6, column=4)

expb.grid(row=7, column=0)
zero.grid(row=7, column=1)
egal.grid(row=7, column=2)

root.mainloop()