from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:id>/', views.home, name='posts-home'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('new_post/<int:id>/', views.new_post, name='post-form'),
    path('like/<int:id>/', views.like, name='like'),
    path('add_comment/<int:id>/', views.add_comment, name='add-comment'),
    path('mypost/<int:id>/', views.mypost, name='mypost'),
    path('delete/<int:id>', views.delete, name='post-delete'),
    path('edit/<int:id>/', views.edit, name='post-edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
