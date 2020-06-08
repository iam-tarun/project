from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notification
from profiles.models import Profiles
from django.contrib.auth.models import User
from groups.forms import InvitationForm
from groups.models import GroupUserTable, Invitation
from .models import Notification,SharedItemsList
from .forms import AcceptanceForm,ItemReturnForm
from django.contrib import messages
from userapp.models import Itemlist
from django.db.models import F
from rating.models import Rate,Leaderboard

def show_personal_notification(request, notification_id):
    context = {
        'notification': Notification.objects.get(id=notification_id),
    }
    return render(request, 'notification/personal_notification.html', context)

def show_image_notification(request, notification_id):
    item_notification = Notification.objects.get(id=notification_id)

    context = {
        'notification': Notification.objects.get(id=notification_id),
        'form' : AcceptanceForm()
     }
    if request.method == 'POST':
         form = AcceptanceForm(request.POST)
         if form.is_valid():
             item_notification = Notification.objects.get(id=notification_id)
             if form.cleaned_data['choice'] == 'A':
                 shareditem = item_notification.shareditemslist_set.create(item_name = item_notification.item_name, shared_user = request.user.username,
                                                         borrowed_user = item_notification.curr_user)
                 shareditem.save()
                 x=User.objects.get(username=shareditem.shared_user)
                 y=User.objects.get(username=shareditem.borrowed_user)

                 shared_leaderb = Leaderboard.objects.get(user=x)
                 shared_leaderb.shared_n = F('shared_n') + 1
                 shared_leaderb.save()
                 shared_leaderb = Leaderboard.objects.get(user=x)
                 shared_leaderb.points = F('shared_n')*F('avg_rating')
                 shared_leaderb.save()

                 borrowed_leaderb = Leaderboard.objects.get(user=y)
                 borrowed_leaderb.borrowed_n = F('borrowed_n') + 1
                 borrowed_leaderb.save()

                 messages.success(request,'You accepted to give your item to ' + item_notification.curr_user)
                 Item = Itemlist.objects.get(name=request.user, item = item_notification.item_name)
                 Item.ItemStatus = "NOT-AVAILABLE"
                 Item.save()
                 item_notification.viewed = True
                 item_notification.save()
                 return redirect('/dashboard')
             elif form.cleaned_data['choice'] == 'R':
                 item_notification.delete()
                 return redirect('/notifications')
    return render(request, 'notification/item_notification.html', context)

def show_group_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    i = Invitation.objects.get(notifId=notification_id)

    context = {
        'notification': Notification.objects.get(id=notification_id),
        'groupuser': GroupUserTable.objects.get(user=request.user, status=9, group_id=i.groupid),
        'form': InvitationForm()
    }
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

    return render(request, 'notification/group_notification.html', context)

def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return redirect('/dashboard')

def shared_items(request, id):
    shared_item = SharedItemsList.objects.get(id=id)
    context = {
           's_item' : SharedItemsList.objects.get(id=id),
           'form' : ItemReturnForm()
    }
    if request.method == "POST":
        form = ItemReturnForm(request.POST)
        if form.is_valid():
            shared_item = SharedItemsList.objects.get(id=id)
            if form.cleaned_data['choice'] == 'Y':
                Item = Itemlist.objects.get(name=request.user, item = shared_item.item_name)
                Item.ItemStatus = "AVAILABLE"
                Item.save()
                x = shared_item.borrowed_user
                shared_item.delete()
                return redirect('give-rating',usrname=x)
            else:
                return redirect('/dashboard')

    return render(request, 'notification/shared_items.html', context)

def borrowed_items(request, id):
    context = {
           'b_item' : SharedItemsList.objects.get(id=id)
    }
    return render(request, 'notification/borrowed_items.html' , context)

def loggedin_a(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL"),
        'sent_notifications': Notification.objects.filter(type="Personal"),
    }
    return render(request, 'notification/view_a_notifications.html', context)

def loggedin_p(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(user=request.user, viewed=False, type="Personal"),
        'sent_notifications': Notification.objects.filter(type="Personal"),
    }
    return render(request, 'notification/view_p_notifications.html', context)

def loggedin_i(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(user=request.user, viewed=False, type="Item"),
        'sent_notifications': Notification.objects.filter(type="Item"),
    }
    return render(request, 'notification/view_i_notifications.html', context)

def loggedin_g(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(user=request.user, viewed=False, type="Group"),
        'sent_notifications': Notification.objects.filter(user=request.user,type="Group"),
    }
    return render(request, 'notification/view_g_notifications.html', context)

def give_i_notification(request, usrname):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'notification/give_item_notification.html', context)

def give_p_notification(request, usrname):
    context = {
       'users' : User.objects.all()
    }
    return render(request, 'notification/give_personal_notification.html', context)

def give_i(request, usrname):
    x = usrname
    a = User.objects.get(username=x)
    b = a.notification_set.create(item_name=request.POST['item_name'], message=request.POST['message'], return_date = request.POST['return_date'],
                                  return_time = request.POST['return_time'], curr_user=request.user.username,type="Item")
    b.save()
    return redirect('/dashboard')

def give_p(request, usrname):
    x = usrname
    a = User.objects.get(username=x)
    b = a.notification_set.create(title=request.POST['title'], message=request.POST['message'], curr_user=request.user.username,type="Personal")
    b.save()
    return redirect('/dashboard')
