from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.models import F
from .models import Rate, Leaderboard, Report
from notification.models import Notification

def give_rating(request, usrname):
    context = {
    'user' : User.objects.get(username=usrname),
    'count': Notification.objects.filter(user=request.user, viewed=False, type="Personal")|
                Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL")|
                Notification.objects.filter(user=request.user, viewed=False, type="Item")|
                Notification.objects.filter(user=request.user, viewed=False, type="Group"),

     'count_a': Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL"),
     'count_i': Notification.objects.filter(user=request.user, viewed=False, type="Item"),
     'count_g': Notification.objects.filter(user=request.user, viewed=False, type="Group"),
     'count_f': Notification.objects.filter(user=request.user, viewed=False, type="Friend"),
    }
    return render(request, 'rating/give_rating.html',context)

def rate(request, usrname):
    x = User.objects.get(username=usrname)
    rateobj = x.rate_set.create(rating = request.POST['rating'])
    rateobj.save()
    borrowed_leaderb = Leaderboard.objects.get(user=x)
    borrowed_leaderb.total_rating = F('total_rating') + rateobj.rating
    borrowed_leaderb.save()
    borrowed_leaderb = Leaderboard.objects.get(user=x)
    borrowed_leaderb.avg_rating = F('total_rating')/F('borrowed_n')
    borrowed_leaderb.points = F('avg_rating')*F('shared_n')
    borrowed_leaderb.save()
    return redirect('dashboard')

def leaderboard(request):
    context = {
    'users' :  Leaderboard.objects.all().order_by('-points'),
    'user_top' : Leaderboard.objects.all().order_by('-points')[0:3],
    'count': Notification.objects.filter(user=request.user, viewed=False, type="Personal")|
                Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL")|
                Notification.objects.filter(user=request.user, viewed=False, type="Item")|
                Notification.objects.filter(user=request.user, viewed=False, type="Group"),

     'count_a': Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL"),
     'count_i': Notification.objects.filter(user=request.user, viewed=False, type="Item"),
     'count_g': Notification.objects.filter(user=request.user, viewed=False, type="Group"),
     'count_f': Notification.objects.filter(user=request.user, viewed=False, type="Friend"),
    }
    return render(request, 'rating/leaderboard.html', context)

def give_report(request, usrname):
    context = {
    'user' : User.objects.get(username=usrname),
    'count': Notification.objects.filter(user=request.user, viewed=False, type="Personal")|
                Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL")|
                Notification.objects.filter(user=request.user, viewed=False, type="Item")|
                Notification.objects.filter(user=request.user, viewed=False, type="Group"),

     'count_a': Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL"),
     'count_i': Notification.objects.filter(user=request.user, viewed=False, type="Item"),
     'count_g': Notification.objects.filter(user=request.user, viewed=False, type="Group"),
     'count_f': Notification.objects.filter(user=request.user, viewed=False, type="Friend"),
    }
    return render(request, 'rating/give_report.html', context)

def report(request, usrname):
     a = User.objects.get(username=usrname)
     reportobj = a.report_set.create(report = request.POST['report'])
     reportobj.save()
     return redirect('dashboard')
