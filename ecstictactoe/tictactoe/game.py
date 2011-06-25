# Tic-tac-Toe 
# javascript
# 2011 Eric Schug
# 
# tictactoe

import copy

# 'X' is computer
# 'O' is human
play={'board':[['','',''],['','',''],['','','']],
    'key': 2323, # anti-cheat key
    }
class TicTacToe:
    'computer is X, player is O'
    # status types for board moved
    DONE = 'Done' # game is over
    FINAL = 'Final' # one move left make it
    EMPTY = 'Empty' # board is empty
    ONCHECK = 'OnCheck' # Opponent has been check make winning move
    CHECKED = 'Checked' # Currently Checked
    def __init__(self, play=None):
        self.board=[['','','']['','','']['','','']]
        if play and isValidBoard(play):
            self.board=copy.deepcopy(play['board'])
        
    @staticmethod
    def isValidBoard(play):
        '''check that board from user is valid,
        return: Bool
        '''        
        try:
            board=play['board']
            if len(board) != 3:
                return False
            for row in board:
                if len(row) !=3:
                    return False
                
                for cell in row:
                    if cell not in ['X','O','']:
                        return False
            
            if play['key'] != 2323:
                return False
        except:
            return False
        return True
    def anyMove(self):
        ''' perform any move'''
        for irow in range(3):
            for icell in range(3):
                if self.board[irow][icell] == '':
                    self.board[irow][icell] = 'X'
    def checkMove(self):
        'perform winning move'
        self.anyMove()
        
    def blockMove(self):
        'perform a block move'
        self.anyMove()
                            
    def calcCounts(self):
        self.emptyCounts=0
        for row in self.board:
            for cell in row:
                if cell == '':
                    self.emptyCounts += 1
                
    def status(self):
        '''determine status'''
        self.calcCounts()
        if self.emptyCounts == 0:
            self.status = EMPTY
        elif self.emptyCounts == 1:
            self.status = FINAL
        elif self.emptyCounts == 1:
            self.status = FINAL
                
        
    def move(self):
        '''perform computer move'''
        if self.status == EMPTY:
            self.anyMove()
        elif self.status == FINAL:
            self.anyMove()
        elif self.status == ONCHECK:
            self.checkMove()
        elif self.status == CHECKED:
            self.blockMove()
        else:
            self.anyMove()


    def getPlay(self):
        'get current play'
        return {'board':copy.deepcopy(self.board), 'key':'2323', 'status':self.status, 'winner':self.winner}
   
    def __str__(self):
        def emptyToSpace(s):
            if (s == ''):
                return '   '
            else:
                return ' '+s+' '
        board = ['|'.join([emptyToSpace(cell) for cell in row])+'\n' for row in self.board]
        s = ('-'*11+'\n').join(board)
        return s

