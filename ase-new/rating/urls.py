from django.urls import path, include
from . import views as rate_views

urlpatterns = [
    path('give_rating/<str:usrname>', rate_views.give_rating)
 ]
