from django.urls import path, include
from . import views
from django.conf.urls import url
from profiles import views as profileviews
urlpatterns = [
    path('<int:id>/', views.todoView, name='announcements'),
    path('add/<int:id>/', views.printer, name='add'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    path('viewprofile/<str:name>/', profileviews.view_profile, name='view_profile'),
]
