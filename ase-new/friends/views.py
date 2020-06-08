from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import FriendRequestForm, AcceptForm
from django.contrib import messages
from notification.models import Notification
from .models import Friends
from rating.models import Leaderboard

def friends(request):
    context = {
        'form': FriendRequestForm(),
        'frnds': Friends.objects.all(),
        'requests' : Notification.objects.filter(user=request.user, viewed=False, type="Friend"),
        'count': Notification.objects.filter(user=request.user, viewed=False, type="Personal")|
                    Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL")|
                    Notification.objects.filter(user=request.user, viewed=False, type="Item")|
                    Notification.objects.filter(user=request.user, viewed=False, type="Group"),

         'count_a': Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL"),
         'count_i': Notification.objects.filter(user=request.user, viewed=False, type="Item"),
         'count_g': Notification.objects.filter(user=request.user, viewed=False, type="Group"),
         'count_f': Notification.objects.filter(user=request.user, viewed=False, type="Friend"),
    }
    if request.method == 'POST':
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            if User.objects.get(username=form.cleaned_data['username']):
                ntf = User.objects.get(username=form.cleaned_data['username']).notification_set.create(
                    title=request.user.username, message='Be my friend!!',curr_user=request.user.username, type="Friend")
                ntf.save()
                messages.success(request, 'Friend Request sent to ' + ntf.user.username)

    return render(request, 'friends/myfriends.html', context)


def show_friend_request(request, notification_id):
    ntf = Notification.objects.get(id=notification_id)
    context = {
       'notification' : Notification.objects.get(id=notification_id),
       'form' : AcceptForm()
    }

    if request.method == 'POST':
        form = AcceptForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['choice'] == 'A':
                frnds = Friends(user1=request.user.username,user2=ntf.curr_user)
                frnds.save()
            ntf.delete()
        return redirect('dashboard')

    return render(request, 'friends/friend_notification.html', context)

def user_profile(request, usrname):
    x = User.objects.get(username=usrname)
    context = {
    'user' : User.objects.get(username=usrname),
    'user_leaderboard' : Leaderboard.objects.get(user=x),
    'count': Notification.objects.filter(user=request.user, viewed=False, type="Personal")|
                Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL")|
                Notification.objects.filter(user=request.user, viewed=False, type="Item")|
                Notification.objects.filter(user=request.user, viewed=False, type="Group"),

     'count_a': Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL"),
     'count_i': Notification.objects.filter(user=request.user, viewed=False, type="Item"),
     'count_g': Notification.objects.filter(user=request.user, viewed=False, type="Group"),
     'count_f': Notification.objects.filter(user=request.user, viewed=False, type="Friend"),
    }
    return render(request, 'friends/user_profile.html', context)
