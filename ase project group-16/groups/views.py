from django.shortcuts import render, redirect
from .forms import GroupCreationForm, MemberAdditionForm, LeaveGroupForm
from .models import GroupUserTable, GroupTable, Invitation
from userapp.models import Itemlist
from userapp.forms import UserFilter
from django.contrib.auth.models import User
from notification import views as notify_views
from notification.models import Notification
from django.contrib import messages


# Create your views here.
def create_group(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.admin = request.user
            form.save()
            new_group = GroupTable.objects.last()
            group_user = GroupUserTable.objects.create(group=new_group, user=request.user, status=1)
            group_user.save()
            return redirect('dashboard')
    else:
        form = GroupCreationForm()
    context = {
        'form': form
    }
    return render(request, 'groups/create-group.html', context)


def home(request, id):
    group = GroupTable.objects.get(id=id)
    users = GroupUserTable.objects.filter(group=group, status=1)
    items = Itemlist.objects.filter(name__groupusertable__group=group, name__groupusertable__status=1)
    user_filter = UserFilter(request.GET, queryset=items)
    l_form = LeaveGroupForm()

    context = {
        'group': group,
        'filter': user_filter,
        'users': users,
        'form': MemberAdditionForm(),
        'count': Notification.objects.filter(user=request.user, viewed=False),
        'l_form': l_form,
        'items': items,
    }
    if request.method == 'POST':
        form = MemberAdditionForm(request.POST)
        if form.is_valid():
            if User.objects.get(username=form.cleaned_data['username']):
                try:
                    groupuser = GroupUserTable.objects.create(group=group,
                                                              user=User.objects.get(username=form.cleaned_data[
                                                                  'username']), status=9)
                    ntf = User.objects.get(username=form.cleaned_data['username']).notification_set.create(
                        title='Group invitation', message='You are invited to join ' + groupuser.group.name,
                        curr_user=request.user.username)
                    ntf.save()
                    messages.success(request, 'invitaion sent to ' + ntf.user.username)
                    i = Invitation.objects.create(groupid=id, notifId=ntf.id)
                    i.save()
                    groupuser.save()
                    return render(request, 'groups/group-home.html', context)
                except:
                    return render(request, 'groups/group-home.html', context)
        if request.method == 'POST':
            l_form = LeaveGroupForm(request.POST)
            if l_form.is_valid():
                if l_form.cleaned_data['choice'] == 'Y':
                    group_user = GroupUserTable.objects.get(user=request.user, group=group)
                    grouptable = GroupTable.objects.get(id=group.id)
                    if grouptable.admin == request.user:
                        grouptable.delete()
                    group_user.delete()
                return redirect('dashboard')

    return render(request, 'groups/group-home.html', context)
