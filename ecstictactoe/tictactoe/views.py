# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json
import game
import random
from ascii import ascii

messages = {'':['base message'],
            'X':['X message'],
            'O':['O message'],
            'Draw':['Draw message'],
            }
def gameView(request):
    'Tic Tac Toe game, shows board'
    # play is the current 
    play={'board':[['','',''],['','',''],['','','']],
        'winner':'',
        'status':'',
        }
    art=''
    message=""
    if (request.method == 'GET'):
        # no ajax support
        if('board' in request.GET):
            board=request.GET['board']
            if(len(board)==9):
                for i in range(9):
                    row = i/3
                    col = i%3
                    if(board[i]=='_'):
                        play['board'][row][col] = ''
                    elif(board[i]=='X'):
                        play['board'][row][col] = 'X'
                    elif(board[i]=='O'):
                        play['board'][row][col] = 'O'                    
            if('cell' in request.GET):
                cell=request.GET['cell']
                row=int(cell[0])
                col=int(cell[1])
                play['cell']=(row,col)
                if(row>=0 and row<3 and col>=0 and col<3):
                     if(play['board'][row][col]==''):
                        play['board'][row][col] = 'O'
                        play['key']=2323
                        if (game.TicTacToe.isValidBoard(play)):
                            gamemdl=game.TicTacToe(play)
                            gamemdl.move()
                            play=gamemdl.getPlay()
                            # message from computer
                            if(play['winner'] in messages):
                                message=random.choice(messages[play['winner']]);
                            else:
                                message=random.choice(messages['']);
                            if(play['winner']=='X'):
                                art=random.choice(ascii)
                            else:
                                art='';
    status=str(play)
    #simplified board
    board=''.join(['_' if x=='' else x for x in  play['board'][0]]+
        ['_' if x=='' else x  for x in play['board'][1]]+
        ['_' if x=='' else x for x in  play['board'][2]])
    return render_to_response('tictactoe/index.html', {'play': play,'board':board,'gameurl':reverse(gameView),'status':status, 'message':message, 'art':art})
    
def getmove(request):
    'tic tac toe get computer move json'
    if (request.is_ajax()):
        try:
            play=json.loads('{}')
            if (1): # is valid
                #generate computer move
                #dump move
                jsonPlay=json.dumps(play)
            else:
                jsonPlay=json.dumps({'error':'Connection failed'})
        except:
            jsonPlay=json.dumps({'error':'Connection failed'})
        return HttpResponse(jsonPlay,'application/json')
    else:
        return HttpResponseRedirect('/')
    

