import os
import tkinter
import tkinter as ScrolledText
from tkinter import *
from tkinter import messagebox
clear = lambda: os.system('cls')
def btntext():
    code_console()
def message_debut():
    print('Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32')
    print('use help')
    code_console
def clearssss():
    clear()
    clear()
    message_debut()
def jsp():
    nom = input('quel nom voulez-vous mettre? :')
    haut = input('quel hauteur voulez-vous mettre? :')
    large = input('quel largeur voulez-vous mettre? :')
    tk = Tk()
    tk.title(nom)
    canvas = Canvas(tk, width=(haut), height=(large), bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()
    code_console()
def jsproot():
    nom = input('quel nom voulez-vous mettre? :')
    haut = input('quel hauteur voulez-vous mettre? :')
    large = input('quel largeur voulez-vous mettre? :')
    root = tkinter.Tk()
    root.title(nom)
    canvas = Canvas(tk, width=(haut), height=(large), bd=0, highlightthickness=0)
    canvas.pack()
    root.update()
    code_console()
def jp():
    print("désolée mais ce n'est pas possible.")
    print("ous vous demandons de fermer l'autre fenêtre")
    print("et en ouvrir une autre.")
    jsp()
def elser():
    print(">>>cette commande n'est pas disponible ou inexistante. utilise help")
    code_console()
#jsp
def loop_Fausse():
    for x in range(1, 200):
        print('dans besoin rrrrrrr')
        clear()
        print('Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32')
        print('use help')
    code_console()
#le help
def help_of_code_console():
    print('>>>list:')
    print('>>>import turtle/import time')
    print('>>>help / clear / tk.tk')
    print('>>>print / tk.tk.change title')
    print('>>>turtle.forward(en fase de test)/turtle.left(en fase de test)')
    print('>>>button/message.box/root.tk')
    code_console()
#l'endroit ou tu code ce que tu peux
def code_console():    
    commande =  input('')
    if commande == 'import turtle':
        import turtle
        t = turtle.pen()
        code_console()
    if commande == 'import time':
        import time
        code_console()
    if commande == 'loop':
        loop_Fausse()
    if commande == 'clear' :
        clearssss()
    if commande == 'print':
        print = input('>>>que voulez vous mettre dans ce print? :')
        print(print)
        code_console()
    if commande == '':
        code_console()
    if commande == 'help':
        help_of_code_console()
    if commande == 'tk.tk' :
        jsp()
    if commande == 'import tkinter':
        import tkinter as tk
        print("importé")
        code_console()
    if commande == 'tk.tk.change title':
        jp()
    if commande == 'turtle.forward':
        forward = input('de combien veux-tu avancer? :')
        turtle.forward(forward)
        code_console()
    if commande == 'button':
        text = input('quel est le text que vous voulez mettre? :')
        btn = Button(tk, text=text)
        btn.pack()
        code_console
    if commande == 'message.box':
        quoi = input('quel sorte de message box veux-tu mettre? :')
        if quoi == 'info':
            txt = input("quel est le text que tu veux mettre à l'interrieur? :")
            titre = input('quel titre veux-tu mettre? :')
            messagebox.showinfo((titre), (txt))
            code_console()
        if quoi == 'error':
            txt = input("quel est le text que tu veux mettre à l'interrieur? :")
            titre = input('quel titre veux-tu mettre? :')
            messagebox.showerror((titre), (txt))
            code_console()
        if quoi == 'warning':
            txt = input("quel est le text que tu veux mettre à l'interrieur? :")
            titre = input('quel titre veux-tu mettre? :')
            messagebox.showwarning((titre), (txt))
        if quoi == 'askyesno':
            txt = input("quel est le text que tu veux mettre à l'interrieur? :")
            titre = input('quel titre veux-tu mettre? :')
            messagebox.askyesno((titre), (txt))
    if commande == 'root.tk':
        jsproot()
    if commande == "chattropMIMI":
        print('le fat trop mignion du 33 est...')
        print('')
        print('')
        print('')
        print('')
        print('MIMI!!!! avec ∞ : point! et 100% dans gens ont voté pour lui!')
        code_console()
    else :
        elser()
 #l'endroit ou tu commence (la mise en place)
print('Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32')
print('use help')
code_console()
