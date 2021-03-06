from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.template import loader
from direct.models import Message
from django.contrib import messages 

# Create your views here.
@login_required
def inbox(request):
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=user, recipient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    
        context = {
            'directs' : directs,
            'messages' : messages,
            'active_direct' : active_direct,
        }
    #template = loader.get_template('direct.html')
    return render(request, 'direct.html', context)
    #return render_to_response(request, 'direct.html', context)
    #return HttpResponse(template, render(context, request))

@login_required
def Directs(request, username):
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)
    #username = request.get['username']
    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0

    context = {
        'directs':directs,
        'messages':messages,
        'active_direct':active_direct,
    }        
    #template = loader.get_template('direct/direct.html')
    return render(request, 'direct.html', context)
    #return HttpResponse(template.render(context, request))

@login_required
def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')
    
    
    if request.method == 'POST':
        try:
            to_user = User.objects.get(username=to_user_username)
            Message.send_message(from_user, to_user, body)
        except User.DoesNotExist:
            to_user = None
        return redirect('inbox')
    else:
      return HttpResponseBadRequest()