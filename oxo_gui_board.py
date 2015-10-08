from Tix import Tk
from Tkinter import Frame, Button, Label, Menu
from _tkinter import mainloop
from tkMessageBox import showinfo, showerror, askyesno

import oxo_logic

top = Tk()

def buildMenu(parent):
    menus = (
             ("File", (("New", evNew),
                       ("Resume", evResume),
                       ("Save", evSave),
                       ("Exit", evExit))),
             ("Help", (("Help", evHelp),
                       ("About", evAbout)))
             )   
    menubar = Menu(parent)
    for menu in menus:
        m = Menu(parent)
        for item in menu[1]:
            m.add_command(label=item[0], command=item[1])
        menubar.add_cascade(label=menu[0], menu=m)
        
    return menubar

def evNew():
    status['text'] = 'Playing Game'
    game2cells(oxo_logic.newGame())
    
def evResume():
    status['text']='Playing Game'
    game = oxo_logic.restoreGame()
    game2cells(game)
    
def evSave():
    game = cells2game()
    oxo_logic.saveGame(game)
    
def evExit():
    if status['text'] == 'Playing Game':
        if askyesno("Quitting", "Do you want to save the game before quitting?"):
            evSave()
    top.quit()
    
def evHelp():
    showinfo('help','''
    File=>New: starts a new game of tic-tac-toe
    File=>Resume: restores the last saved game and commences play
    File=>Save: Saves current game.
    File=>Exit: quits, promts to save active game
    Help=>Help: shows this page
    Help=>About: Shows information about the program and author''')
    
def evAbout():
    showinfo("About", "Tic-tac-toe game GUI demo by Alan Gauld")
    
def evClick(row,col):
    if status['text']=='Game Over':
        showerror('Game over', 'Game over!')
        return
    
    game = cells2game()
    index = (3*row) + col
    result = oxo_logic.userMove(game, index)
    game2cells(game)
    
    if not result:
        result = oxo_logic.computerMove(game)
        game2cells(game)
    if result == 'D':
        showinfo("Result", "It's a Draw")
        status['text']='Game Over'
    else:
        if result == "X" or result == "O":
            showinfo("Result", "The winner is: {}".format(result))
            status['text']='Game Over'

def game2cells(game):
    table = board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            table.grid_slaves(row=row,column=col)[0]['text']=game[3*row+col]
                
def cells2game():
    values =[]
    table = board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            values.append(table.grid_slaves(row=row, column=col)[0]['text'])
    return values
    
def buildBoard(parent):
    outer = Frame(parent, border=2, relief ="sunken")
    inner = Frame(outer)
    inner.pack()
    
    for row in range(3):
        for col in range(3):
            cell = Button(inner, text=" ", width="5", height="2",
                          command = lambda r=row, c=col : evClick(r,c))
            cell.grid(row=row, column=col)
    return outer

mbar = buildMenu(top)
top["menu"] = mbar

board = buildBoard(top)
board.pack()
status = Label(top, text="Playing Game", border=0,
               background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True)

mainloop() 
    
    
    