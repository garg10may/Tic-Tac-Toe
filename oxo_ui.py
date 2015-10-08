'''CLI user Interface for Tic-Tac-Toe game.
    Use as the main program, no reusable functions'''
    
import oxo_logic
import tkMessageBox as mb
import Tkinter

menu = ['Start new game', 'Resume saved game', 'Display help', 'Quit']

def getMenuChoice(aMenu):
    '''getMenuChoice(aMenu) -> int
    
        takes a list of strings as input,
        displays as a numbered menu and
        loops until user selects a valid number'''
    
    for  index, item in enumerate(aMenu, start=1):
        print str(index) +  "\t" +  item
        
    choice = int(raw_input('\nChoose a menu option:'))
    return choice    

def startGame():
    return oxo_logic.newGame()

def resumeGame():
    return oxo_logic.restoreGame()

def displayHelp():
    print '''
    Start new game: starts a new game of tic-tac-toe
    Resume saved game: restores the last saved game and commences play
    Display help: shows this page
    Quit: quits the application
    '''
    
def Quit():
    print "Goodbye"
    raise SystemExit

def executeChoice(choice):
    dispatch = [startGame, resumeGame, displayHelp, Quit]
    game = dispatch[choice-1]()
    if game:
        playGame(game)

def printGrid():
    grid = '''
    1 | 2 | 3
    ---------  
    4 | 5 | 6  
    ---------  
    7 | 8 | 9  
    '''
    print grid
    
def printGame(game):
    display = '''
    {} | {} | {}
    ---------
    {} | {} | {}
    ---------
    {} | {} | {}
    '''
    print display.format(*game)
    
def playGame(game):
    result =""
    printGrid()
    while not result:
        printGame(game)
        choice = raw_input('Cell[1-9 or q to quit]:')
        if choice.lower()[0] == 'q':
            save = raw_input('save game before quitting? [y/n]?')
            if save.lower()[0] =='y':
                oxo_logic.saveGame(game)
            quit()
        else:
            try:
                cell = int(choice)-1
                if not (0 <= cell <= 8): #check range
                    raise ValueError
            except ValueError:
                print "Choose a number between 1 and 9 or 'q' to quit"
                continue
        try: 
            result = oxo_logic.userMove(game,cell)
        except ValueError:
            print ("Choose any empty cell")
            continue
        if not result:
            result = oxo_logic.computerMove(game)
        if not result:
            continue
        elif result == 'D':
            printGame(game)
            print "It's a draw"
        else:
            printGame(game)
            mb.showinfo("Winner", result)  
            print ("Winner is ", result)
            
def main():
    top = Tkinter.Tk()
    top.withdraw()
    while True:
        choice = getMenuChoice(menu)
        executeChoice(choice)           
           
if __name__ == "__main__": 
    main()
    