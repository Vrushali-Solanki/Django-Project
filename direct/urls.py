from django.urls import path
from . import views
from direct.views import inbox, Directs, SendDirect


urlpatterns = [
    path('', inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send_direct'),
    #path('send/', SendDirect, name='send_direct'),
]
    