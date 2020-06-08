from django.shortcuts import render, redirect
from .forms import Usersignupform
from django.contrib import messages
from email.message import EmailMessage
import smtplib


def homepage(request):
    return render(request, template_name='homepage/home.html', context=None)


def signup(request):
    form = Usersignupform()

    if request.method == 'POST':
        form = Usersignupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')

    return render(request, template_name='homepage/signup.html', context={'form': form})


def forgotpassword(request):
    return render(request, template_name="homepage/fg.html", context=None)


def about(request):
    return render(request, 'homepage/about.html')
