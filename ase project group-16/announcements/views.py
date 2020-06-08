from django.shortcuts import render, redirect
from .forms import AnnouncementForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from groups.models import GroupTable, GroupUserTable
from groups.forms import LeaveGroupForm

@login_required
def printer(request, id):
    group =  GroupTable.objects.get(id=id)
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.groupid = id
            instance.save()
            return redirect('announcements', group.id )
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/test.html', {'form': form, 'group': group})


@login_required
def delete(request, id):
    post_to_delete = Post.objects.get(id=id)
    post_to_delete.delete()
    x = Post.objects.all()
    return render(request, 'announcements/test2.html', {'all_items': x})


@login_required
def todoView(request, id):
    group = GroupTable.objects.get(id=id)
    users = GroupUserTable.objects.filter(group=group)
    l_form = LeaveGroupForm()
    x = Post.objects.filter(groupid=group.id).order_by('-date_created')
    page = request.GET.get('page', 1)
    paginator = Paginator(x, 3)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)

    context = {
        'all_items' : announcements,
        'group': group,
        'users':users,
        'l_form':l_form,
    }

    return render(request, 'announcements/test2.html', context)
