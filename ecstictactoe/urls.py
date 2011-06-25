# Tic-tac-Toe 
# javascript
# 2011 Eric Schug
# 
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin

urlpatterns = patterns('',
    # board
    (r'^$', 'ecstictactoe.tictactoe.views.gameView'),
    # move (ajax)
    (r'^move/$', 'ecstictactoe.tictactoe.views.getmove'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
