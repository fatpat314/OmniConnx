from django.urls import path
from message.views import Inbox, UserSearch, Directs, NewConversation, SendDirect
urlpatterns = [
   	path('inbox/', Inbox, name='inbox'),
   	path('message/<username>', Directs, name='directs'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),

]
