from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Bpost, Comments
from django.contrib.auth.models import User
from groups.models import GroupUserTable, GroupTable


# Create your views here


@login_required
def home(request, id):
    author = request.user.id
    tposts = Bpost.objects.filter(group_id=id)
    tlist = []
    for p in tposts:
        likearray = list(map(int, p.likelist.split()))
        if author in likearray:
            tlist.append(p.id)

    context = {
        'posts': Bpost.objects.filter(group_id=id),
        'liked': tlist,
        'comments': Comments.objects.all(),
        'iid': id,
        'group': GroupTable.objects.get(id=id),
        'users': GroupUserTable.objects.filter(group=GroupTable.objects.get(id=id)),
    }
    return render(request, 'blogpost/home.html', context)


def mypost(request, id):
    author = request.user
    li = Bpost.objects.all()
    List = []
    for obj in li:
        if obj.author == author:
            List.append(obj)
    context = {
        'posts': List,
        'comments': Comments.objects.all(),
        'id': id,
        'group': GroupTable.objects.get(id=id),
    }
    return render(request, 'blogpost/mypost.html', context)


def delete(request, id):
    if request.method == "POST":
        objid = request.POST.get('objid')
        obj = Bpost.objects.get(id=objid)
        obj.delete()
        return redirect('mypost', id)
    return redirect('mypost', id)


def edit(request, id):
    if request.method == "POST":
        objid = request.POST.get('objid')
        obj = Bpost.objects.get(id=objid)
        content = request.POST.get('content')
        if len(content) != 0:
            obj.content = content
            obj.save()
        return redirect('mypost', id)
    return redirect('mypost', id)


def form(request):
    context = {
        'Users': User.objects.all()

    }
    return render(request, 'blogpost/form.html', context)


def about(request):
    return render(request, 'blogpost/about.html')


def add_comment(request, id):
    if request.method == "POST":
        content = request.POST.get('content')
        objid = request.POST.get('objid')
        author = request.user.username
        published_on = timezone.now()
        if len(content) != 0:
            Comments.objects.create(content=content, date_posted=published_on, objid=objid, author=author).save()
            return redirect('posts-home', id)
        else:
            return redirect('posts-home', id)
    return redirect('posts-home', id)


def like(request, id):
    if request.method == "POST":
        author = request.user.id
        obj_id = request.POST.get('objid')
        post = Bpost.objects.get(id=obj_id)
        likelist = post.likelist

        likearray = list(map(int, likelist.split()))
        likenumber = post.likes

        if author in likearray:
            likearray.remove(author)
            likenumber = likenumber - 1
            likelist = ""
            for nums in likearray:
                likelist = likelist + str(nums) + " "
        elif author not in likearray:
            likearray.append(author)
            likenumber = likenumber + 1
            likelist = ""
            for nums in likearray:
                likelist = likelist + str(nums) + " "

        post.likes = likenumber
        post.likelist = likelist
        post.save()
        return redirect('posts-home', id)
    return redirect('posts-home', id)


def new_post(request, id):
    if request.method == "POST":
        content = request.POST.get('content')

        author = request.user
        image = request.FILES['image']
        published_on = timezone.now()
        Bpost.objects.create(content=content, date_posted=published_on, likelist='', likes=0, author=author,
                             image=image, group=GroupTable.objects.get(id=id)).save()
        return redirect('posts-home', id)
    context = {
        'id': id,
        'group': GroupTable.objects.get(id=id),
        'users': GroupUserTable.objects.filter(group_id=id),
    }
    return render(request, 'blogpost/form.html', context)
