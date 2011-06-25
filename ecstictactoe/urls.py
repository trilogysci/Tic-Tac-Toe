# Tic-tac-Toe 
# javascript
# 2011 Eric Schug
# 
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin

urlpatterns = patterns('',
    # board
    (r'^$', 'ecstictactoe.tictactoe.views.game'),
    # move (ajax)
    (r'^move/$', 'ecstictactoe.tictactoe.views.move'),

)
