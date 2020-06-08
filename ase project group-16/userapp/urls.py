from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import Itemlistview, Itemlistdetailview, ItemlistCreateview, ItemlistUpdateview, Itemlistdeleteview, \
    UserItemlist

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('itemlist/<int:pk>/', Itemlistdetailview.as_view(), name='Itemlist-detail'),
    path('itemlist/new/', ItemlistCreateview.as_view(), name='Itemlist-create'),
    path('itemlist/<int:pk>/update/', ItemlistUpdateview.as_view(), name='Itemlist-update'),
    path('itemlist/<int:pk>/delete/', Itemlistdeleteview.as_view(), name='Itemlist-delete'),
    path('user/<str:username>', UserItemlist.as_view(), name='user-itemslist'),
]
