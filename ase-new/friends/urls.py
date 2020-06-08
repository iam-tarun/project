from django.conf.urls import url
from django.urls import path
from friends import views as friend_views

urlpatterns = [
 path('friends/',friend_views.friends, name='friends'),
]
]
