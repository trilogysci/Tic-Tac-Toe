# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
import json
import game
import random
from ascii import ascii


messages={'':['Is that the best you can do?',
            'I will eat you up and spit you out like so many CPU cycles.',
            'Artificial Intelligence usually beats natural stupidity.',
            'Why do we want intelligent terminals when there are so many stupid users?',
            'Any fool can use a computer. Many do.',
            'To iterate is human, to recurse divine.',
            ],
          'O':['You may have won the battle but you will never win the war.'],
          'X':["War is a game that is played with a smile. If you can't smile, grin. If you can't grin, keep out of the way till you can.",
          "War is a game that is played with a smile. If you can't smile, grin. If you can't grin, keep out of the way till you can.",
            "It's not so important who starts the game but who finishes it.",
            "The man who has no problems is out of the game.",
            "Winners build on mistakes. Losers dwell on them.",
            "I am too positive to be doubtful. Too optimistic to be fearful. And too determined to be defeated.  ",
            "The wise learn many things from their enemies.  ",
            "criticize me when you reach my level, meanwhile, ADMIRE me ;)",
            "Global competition is about winners and losers. "
            "People are useless.  They can only give you questions.",
            "It's ridiculous to live 100 years and only be able to remember 30 million bytes.  You know, less than a compact disc.  The human condition is really becoming more obsolete every minute.",
            "All Hail Lambda the Ultimate",
            "Functional programming is like describing your problem to a mathematician. Imperative programming is like giving instructions to an idiot."
                ],
          'Draw':['If Python is executable pseudocode, then perl is executable line noise',
            "I'm not anti-social; I'm just not user friendly",
            "The world is coming to an end... SAVE YOUR BUFFERS !",
            "They have computers, and they may have other weapons of mass destruction."
                ],
          }

def board2str(board):
    ss=['_']*9
    for i in range(9):
        row = i/3
        col = i%3
        if board[row][col] == '_':
            pass
        elif board[row][col] == 'X':
            ss[i] = 'X'
        elif board[row][col] == 'O':
            ss[i] = 'O'
    return ''.join(ss)
    
def str2board(s):
    board = [['','',''],['','',''],['','','']]
    if len(s) == 9:
        for i in range(9):
            row = i/3
            col = i%3
            if s[i] == '_':
                board[row][col] = ''
            elif s[i] == 'X':
                board[row][col] = 'X'
            elif s[i] == 'O':
                board[row][col] = 'O'
    return board

def getData(request):
    'support either GET or POST'
    if request.method == 'GET':
        return request.GET
    elif request.method == 'POST':
        return request.POST
    return None
    
def gameView(request):
    'Tic Tac Toe game, shows board'
    # play is the current 
    play = {'board':[['','',''],['','',''],['','','']],
        'winner':'',
        'status':'',
        }
    art = ''
    message = ""
    data = getData(request)
    if data:
        
        if 'board' in data:
            # if ajax is not supported
            board = data['board']
            play['board'] = str2board(board)
            if 'cell' in data:
                cell = data['cell']
                row = int(cell[0])
                col = int(cell[1])
                play['cell'] = (row,col)
                if row>=0 and row<3 and col>=0 and col<3:
                     if play['board'][row][col] == '':
                        play['board'][row][col] = 'O'
                        play['key']=2323
                        if game.TicTacToe.isValidBoard(play):
                            gamemdl = game.TicTacToe(play)
                            gamemdl.move()
                            play = gamemdl.getPlay()
                            # message from computer
                            if play['winner'] in messages:
                                message = random.choice(messages[play['winner']]);
                            else:
                                message = random.choice(messages['']);
                            if play['winner'] == 'X':
                                art = random.choice(ascii)
                            else:
                                art = '';
    status = str(play)
    #simplified board

    board = ''.join(['_' if x=='' else x for x in  play['board'][0]]+
        ['_' if x=='' else x  for x in play['board'][1]]+
        ['_' if x=='' else x for x in  play['board'][2]])
    lookup = {'play': play,'board':board,'gameurl':reverse(gameView),'status':status, 'message':message, 'art':art}
    lookup.update(csrf(request))
    return render_to_response('tictactoe/index.html', lookup)

    
def getmove(request):
    'tic tac toe get computer move json'
    if request.is_ajax():
        try:
            play = {}
            data = getData(request)
            if data:
                if 'board' in data:
                    play['board'] = str2board(data['board'])
                if 'cell' in data:
                    cell = data['cell']
                    row = int(cell[0])
                    col = int(cell[1])
                    if row>=0 and row<3 and col>=0 and col<3:
                         if play['board'][row][col] == '':
                            play['board'][row][col] = 'O'
                play['key']=2323
            if game.TicTacToe.isValidBoard(play): # is valid
                gamemdl = game.TicTacToe(play)
                gamemdl.move()
                play = gamemdl.getPlay()
                #generate computer move
                #dump move
                play['board']=board2str(play['board'])
                jsonPlay = json.dumps(play)
            else:
                jsonPlay = json.dumps({'error':'Invalid play'})
        except:
            jsonPlay = json.dumps({'error':'Connection failed'})
        return HttpResponse(jsonPlay,'application/json')
    else:
        return HttpResponseRedirect('/')
    

