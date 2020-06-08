from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notification
from profiles.models import Profiles
from django.contrib.auth.models import User
from groups.forms import InvitationForm
from groups.models import GroupUserTable, Invitation


def show_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    try:
        i = Invitation.objects.get(notifId=notification_id)
        if request.method == 'POST':
            form = InvitationForm(request.POST)
            if form.is_valid():
                i = Invitation.objects.get(notifId=notification_id)
                groupuser = GroupUserTable.objects.get(user=request.user, status=9, group_id=i.groupid)
                if form.cleaned_data['choice'] == 'A':
                    groupuser.status = 1
                    groupuser.save()
                elif form.cleaned_data['choice'] == 'R':
                    groupuser.delete()
            notification.delete()
            i.delete()
            return redirect('notifications')
        context = {
            'notification': Notification.objects.get(id=notification_id),
            'groupuser': GroupUserTable.objects.get(user=request.user, status=9, group_id=i.groupid),
            'form': InvitationForm()
        }
    except Invitation.DoesNotExist:
        context = {
            'notification': Notification.objects.get(id=notification_id),
            'form': InvitationForm()
        }
        return render(request, 'notification/notification.html', context)
    return render(request, 'notification/notification.html', context)


def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return redirect('/loggedin')


def loggedin(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(user=request.user, viewed=False),
        'sent_notifications': Notification.objects.all(),
    }
    return render(request, 'notification/view_notifications.html', context)


def give_notification(request, usrname):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'notification/give_notification.html', context)


def give(request, usrname):
    x = usrname
    a = User.objects.get(username=x)
    b = a.notification_set.create(title=request.POST['title'], message=request.POST['message'],
                                  curr_user=request.user.username)
    b.save()
    return redirect('/loggedin')
