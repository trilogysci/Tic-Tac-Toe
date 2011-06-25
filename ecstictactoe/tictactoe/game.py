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

# status types for board moved
DONE = 'Done' # game is over
FINAL = 'Final' # one move left make it
EMPTY = 'Empty' # board is empty
ONCHECK = 'OnCheck' # Opponent has been check make winning move
CHECKED = 'Checked' # Currently Checked
UNKNOWN = 'Unknown' # unknown status
class TicTacToe:
    'computer is X, player is O'
    def __init__(self, play=None):
        self.board=[['','',''],['','',''],['','','']]
        if play and self.isValidBoard(play)[0]:
            self.board=copy.deepcopy(play['board'])
        
    @staticmethod
    def isValidBoard(play):
        '''check that board from user is valid,
        return: Bool, 'Error Message'
        '''        
        try:
            ocount = 0
            xcount = 0
            board=play['board']
            if len(board) != 3:
                return False, 'Row count invalid'
            for row in board:
                if len(row) !=3:
                    return False, 'Cell count invalid'
                # check cell values
                for cell in row:
                    if cell not in ['X','O','']:
                        return False, 'Invalid cell value'
                    if cell == 'X':
                        xcount += 1
                    if cell == 'O':
                        ocount += 1
            # move count must be valid
            if(ocount-xcount>1 or ocount-xcount<0):
                return False, 'Can not have a double move'
            if play['key'] != 2323:
                return False, 'incomplete message'
        except:
            return False, 'incomplete message'
        return True, 'Ok'
    
    def anyMove(self):
        ''' perform any move'''
        for irow in range(3):
            for icell in range(3):
                if self.board[irow][icell] == '':
                    self.board[irow][icell] = 'X'
                    return
        raise "anyMove failed to find emty cell"
    
    def checkMove(self):
        'perform winning move'
        self.anyMove()
        
    def blockMove(self):
        'perform a block move'
        self.anyMove()
                            
    def calcCounts(self):
        'compute data counts'
        self.emptyCounts=0
        for row in self.board:
            for cell in row:
                if cell == '':
                    self.emptyCounts += 1
                
    def updateStatus(self):
        '''determine status'''
        
        self.calcCounts()
        
        self.status = UNKNOWN
        
        if self.emptyCounts == 0:
            self.status = EMPTY
        elif self.emptyCounts == 1:
            self.status = FINAL
        elif self.emptyCounts == 1:
            self.status = FINAL
        
        
    def move(self):
        '''perform computer move'''
        self.updateStatus()
                
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
        # update counts
        self.calcCounts()

    def getPlay(self):
        'get current play'
        return {'board':copy.deepcopy(self.board), 'key':'2323', 'status':self.status, 'winner':self.winner}
   
    def __str__(self):
        def emptyToSpace(s):
            'convert "" to space, and and some space'
            if (s == ''):
                return '   '
            else:
                return ' '+s+' '
        board = ['|'.join([emptyToSpace(cell) for cell in row])+'\n' for row in self.board]
        s = ('-'*11+'\n').join(board)
        return s

