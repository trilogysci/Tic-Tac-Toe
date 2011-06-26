# Tic-tac-Toe 
# javascript
# 2011 Eric Schug
# 
# tictactoe

import copy
import random

# 'X' is computer
# 'O' is human
play={'board':[['','',''],['','',''],['','','']],
    'key': 2323, # anti-cheat key
    }


def boardFlip(board):
    'flip board along the diagonal'
    return [
        [board[0][0],board[1][0],board[2][0]],
        [board[0][1],board[1][1],board[2][1]],
        [board[0][2],board[1][2],board[2][2]]
        ]

def boardRotate(board):
    'rotate the board'
    return [
        [board[2][0],board[1][0],board[0][0]],
        [board[2][1],board[1][1],board[0][1]],
        [board[2][2],board[1][2],board[0][2]]

        ]

def boardDiagonals(board):
    'return the board diagonals'
    return [
        [board[0][0],board[1][1],board[2][2]],
        [board[2][0],board[1][1],board[0][2]]
        ]


# status types for board moved
DONE = 'Done' # game is over
FINAL = 'Final' # one move left make it
EMPTY = 'Empty' # board is empty
ONCHECK = 'OnCheck' # Opponent has been check make winning move
CHECKED = 'Checked' # Currently Checked
UNKNOWN = 'Unknown' # unknown status
PATTERNMATCH = 'PatternMatch' # PatternMatch
LEADINGMOVE = 'LeadingMove' # Move second in a row
CENTERMOVE = 'CenterMove' # Center Move is usually good
ANYMOVE = 'AnyMove' #AnyMove
class TicTacToe:
    'computer is X, player is O'
    def __init__(self, play=None):
        self.status = ''
        self.winner = ''
        self.board = [['','',''],['','',''],['','','']]
        if play and self.isValidBoard(play)[0]:
            self.board = copy.deepcopy(play['board'])
            self.calcCounts()
        
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
            if ocount-xcount>1 or ocount-xcount<0:
                return False, 'Can not have a double move'
            if play['key'] != 2323:
                return False, 'incomplete message'
        except:
            return False, 'incomplete message'
        return True, 'Ok'
    
    @staticmethod
    def randomBoard():
        board = []
        for i in range(3):
            #build rows of random '', 'X' or 'O'
            board.append([['', 'X', 'O'][random.randint(0,2)] for j in range(3)])
        return {'board':copy.deepcopy(board), 'key':2323}
    
    def matchPattern(self,pattern):
        'does the pattern match, after rotations and flips'
        rpatt=pattern
        for i in range(4):
            if rpatt == self.board:
                return i
            rpatt = boardRotate(rpatt)
        rpatt = boardFlip(pattern)
        for i in range(4):
            if rpatt == self.board:
                return i+4
            rpatt = boardRotate(rpatt)
        return None

    @staticmethod
    def transIndex(trans, cellix):
        'transform cell indices apply flip and rotation'
        if cellix==(1,1) or trans==0:
            return cellix
        cellix_out=(cellix[0],cellix[1])
        if trans>=4:
            #flip
            cellix_out = (cellix_out[1],cellix_out[0])
            trans = trans-4
        corners=[(0,0),(2,0),(2,2),(0,2)]
        sides=[(0,1),(1,0),(2,1),(1,2)]
        #rotate
        if cellix_out in corners:
            # get location and apply rotation
            idx=(corners.index(cellix_out)-trans)%4
            cellix_out=corners[idx]
        elif cellix_out in sides:
            # get location and apply rotation
            idx=(sides.index(cellix_out)-trans)%4
            cellix_out = sides[idx]
        return cellix_out
    def getFreeCnt(self):
        'return number of empty cells'
        return self.emptyCnt
    
    def testUserMove(self, ifree):
        'generate a user move based on index of empty cells'
        if ifree<0 or ifree>=self.emptyCount:
            raise ValueError('Invalid ifree %d'%ifree)
        iLoc = 0
        for irow in range(3):
            for icell in range(3):
                if self.board[irow][icell]=='':
                    if ifree == iLoc:
                        self.board[irow][icell] = 'O'
                        return
                    else:
                        iLoc += 1
        self.calcCounts()
    def anyMove(self):
        ''' perform any move'''
        for irow in range(3):
            for icell in range(3):
                if self.board[irow][icell] == '':
                    self.board[irow][icell] = 'X'
                    return
        print self
        raise "anyMove failed to find empty cell"
    
    def checkMove(self):
        'perform winning move'
        # find empty cell within the axis
        # determine which axis is the winning axis
        for iaxis,cnts in enumerate(self.rowCounts):
            if cnts == {'X':2,'O':0}:
                for icell in range(3):
                    if self.board[iaxis][icell] == '':
                        self.board[iaxis][icell] = 'X'
                        self.winner = 'X'
                        break
                return 
        for iaxis,cnts in enumerate(self.colCounts):
            if cnts == {'X':2,'O':0}:
                for icell in range(3):
                    if self.board[icell][iaxis] == '':
                        self.board[icell][iaxis] = 'X'
                        self.winner = 'X'
                        break
                return
        for iaxis,cnts in enumerate(self.diagCounts):
            if cnts == {'X':2,'O':0}:
                if self.board[1][1] == '':
                    self.board[1][1] = 'X'
                    self.winner = 'X'
                elif iaxis == 0:
                    if self.board[0][0] == '':
                        self.board[0][0] = 'X'
                        self.winner = 'X'
                    elif self.board[2][2] == '':
                        self.board[2][2] = 'X'
                        self.winner = 'X'
                else:
                    if self.board[0][2] == '':
                        self.board[0][2] = 'X'
                        self.winner = 'X'
                    elif self.board[2][0] == '':
                        self.board[2][0] = 'X'
                        self.winner = 'X'
                return
        print self
        raise "checkMove: failed to find empty cell"
        
    def blockMove(self):
        'perform a block move'
        # find empty cell within the axis
        # determine which axis is the blocking axis
        for iaxis,cnts in enumerate(self.rowCounts):
            if cnts == {'X':0,'O':2}:
                for icell in range(3):
                    if self.board[iaxis][icell] == '':
                        self.board[iaxis][icell] = 'X'
                        break
                return
        for iaxis,cnts in enumerate(self.colCounts):
            if cnts == {'X':0,'O':2}:
                for icell in range(3):
                    if self.board[icell][iaxis] == '':
                        self.board[icell][iaxis] = 'X'
                        break
                return
        for iaxis,cnts in enumerate(self.diagCounts):
            if cnts == {'X':0,'O':2}:
                if self.board[1][1] == '':
                    self.board[1][1] = 'X'
                elif iaxis == 0:
                    if self.board[0][0] == '':
                        self.board[0][0] = 'X'
                    elif self.board[2][2] == '':
                        self.board[2][2] = 'X'
                else:
                    if self.board[0][2] == '':
                        self.board[0][2] = 'X'
                    elif self.board[2][0] == '':
                        self.board[2][0] = 'X'
                return
        # should not get here

    def leadingMove(self):
        ''' attempt to Perform leading Move
            return True on success
        '''
        # find empty cell within the axis
        # with no 'O' and 1 'X'
        for iaxis,cnts in enumerate(self.rowCounts):
            if cnts == {'X':1,'O':0}:
                for icell in range(3):
                    if self.board[iaxis][icell] == '':
                        self.board[iaxis][icell] = 'X'
                        return True
        for iaxis,cnts in enumerate(self.colCounts):
            if cnts == {'X':1,'O':0}:
                for icell in range(3):
                    if self.board[icell][iaxis] == '':
                        self.board[icell][iaxis] = 'X'
                        return True
        
        for iaxis,cnts in enumerate(self.diagCounts):
            if cnts == {'X':1,'O':0}:
                if self.board[1][1] == '':
                    self.board[1][1] = 'X'
                    return True
                elif iaxis == 0:
                    if self.board[0][0] == '':
                        self.board[0][0] = 'X'
                        return True
                    elif self.board[2][2] == '':
                        self.board[2][2] = 'X'
                        return True
                else:
                    if self.board[0][2] == '':
                        self.board[0][2] = 'X'
                        return True
                    elif self.board[2][0] == '':
                        self.board[2][0] = 'X'
                        return True
        return False
                            
    def calcCounts(self):
        'compute data counts'
        self.emptyCount=0
        for row in self.board:
            for cell in row:
                if cell == '':
                    self.emptyCount += 1
        # check for axis counts, for each axis determine 'X' and 'O' count
        self.rowCounts = [{'X':row.count('X'), 'O':row.count('O')} for row in self.board]
        self.colCounts = [{'X':row.count('X'), 'O':row.count('O')} for row in boardFlip(self.board)]
        self.diagCounts = [{'X':row.count('X'),'O':row.count('O')} for row in boardDiagonals(self.board)]
        
    def updateStatus(self):
        '''determine status'''
        
        def unblockedMax(acc,next):
            '''
            update max accumulator of
            unblocked axis iff one player has atleast one and other player has none
            '''
            if next['X']>0 and next['O'] == 0:
                acc['X'] = max(acc['X'],next['X'])
            elif next['O']>0 and next['X'] == 0:
                acc['O'] = max(acc['O'],next['O'])
            return acc
        
        
        self.calcCounts()
        self.status = UNKNOWN
        
        #merge all axes
        allCounts=self.rowCounts+self.colCounts+self.diagCounts
        
        #find maxes across all axes
        # 'X' : max # of 'X' with no 'O'
        # 'O' : max # of 'O' with no 'X'
        maxes=reduce(unblockedMax, allCounts, {'X':0,'O':0})
        
        #determine status
        if maxes == {'X':3, 'O':3}:
            #WTF!
            self.winner = 'Draw'
            self.status = DONE
        elif maxes['X'] == 3:
            self.winner = 'X'
            self.status = DONE
        elif maxes['O'] == 3:
            self.winner = 'O'
            self.status = DONE
        elif self.emptyCount == 0:
            self.status = DONE
            self.winner = 'Draw'
        elif maxes['X'] == 2:
            self.status = ONCHECK
        elif maxes['O'] == 2:
            self.status = CHECKED
        elif self.emptyCount == 9:
            self.status = EMPTY
        elif self.emptyCount == 1:
            self.status = FINAL
        
    def move(self):
        '''perform computer move'''
        self.updateStatus()
                
        if self.status == DONE:
            pass
        elif self.status == EMPTY:
            self.anyMove()
        elif self.status == FINAL:
            self.anyMove()
        elif self.status == ONCHECK:
            self.checkMove()
        elif self.status == CHECKED:
            self.blockMove()
        elif (self.board[1][1] == ''):
            #empty center is usually good
            self.status = CENTERMOVE
            self.board[1][1] = 'X'
        else:
            found=False
            for pattern,cellix in [
                        ([['O','',''],['','X',''],['','O','']], (2,0)),
                        ([['O','',''],['','X',''],['','','O']], (1,0)),
                        ([['O','',''],['','O',''],['','','X']], (2,0)),
                        ([['','O',''],['O','X',''],['','','']], (0,0)),
                        ([['O','X',''],['','X','O'],['','O','']], (2,0)),
                        ([['X','O',''],['','','O'],['','','']], (1,0)),
                        ([['X','O',''],['O','','X'],['','','O']], (2,0)),
                        ([['O','X',''],['X','','O'],['','O','']], (2,2)),
                        ]:
                match=self.matchPattern(pattern)
                if(match!=None):
                    self.status=PATTERNMATCH
                    cellix_out= self.transIndex(match, cellix)
                    assert self.board[cellix_out[0]][cellix_out[1]] == ''
                    self.board[cellix_out[0]][cellix_out[1]] = 'X'
                    found=True
            if found:
                pass
            elif self.leadingMove():
                self.status = LEADINGMOVE
                pass
            else:
                self.status = ANYMOVE
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

