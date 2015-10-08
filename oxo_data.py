'''oxo_data is the data module for a tic-tac-toe ( or 0x0) game. 
    It saves and restores a game board. The functions are:
        saveGame(game) -> None
        restoreGame() -> game
    Note that no limits are placed on the size of the data. The game implementation
    is responsible for validating all data in and out.
'''

import os.path

game_file = '.oxogame.dat'

def _getPath():
    game_path = os.getcwd()
    return game_path

def saveGame(game):
    path = os.path.join(_getPath(), game_file)
    with open(path, 'w') as gf:
        gamestr = ''.join(game)
        gf.write(gamestr)
        
def restoreGame():
    '''restoreGame() -> game
    
    Restores a game from the data file.
    The game object is a list of characters
    '''
    
    path = os.path.join(_getPath(), game_file)
    with open(path) as gf:
        gamestr = gf.read()
        return list(gamestr)
    
def _test():
    print("path =", _getPath())
    saveGame(list("XO XO OX"))
    print (restoreGame())
    
if __name__ == "__main__" :
    _test()
    
    