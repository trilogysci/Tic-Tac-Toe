# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json

def game(request):
    'Tic Tac Toe game, shows board'
    return render_to_response('tictactoe/index.html',{});
    
def move(request):
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
    

