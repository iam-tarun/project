from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm, BackgroundImageForm
from django.contrib.auth.decorators import login_required
from .models import Profiles
from django.contrib.auth.models import User
from announcements.models import Post
from django.urls import reverse



# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profiles)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profiles)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def changebackground(request):
    if request.method == 'POST':
        b_form = BackgroundImageForm(request.POST, request.FILES, instance=request.user.backgroundimage)
        if b_form.is_valid():
            b_form.save()
            return redirect('back')
    else:
        b_form = BackgroundImageForm(instance=request.user.backgroundimage)
    context = {
        'b_form': b_form
    }
    return render(request, 'profiles/back.html', context)


def view_profile(request, name):
    person = User.objects.get(username=name)
    user_profile = person.profiles
    context = {'profile': user_profile , 'person': person , 'announcements': person.post_set.all()}
    return render(request, 'profiles/viewprofile.html', context)

