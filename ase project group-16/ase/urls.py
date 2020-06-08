from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from notification import views as notify_views



urlpatterns = [
    path('', include('homepage.urls')),
    path('dashboard/', include('userapp.urls')),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('signin/', auth_views.LoginView.as_view(template_name='homepage/signin.html'), name = 'signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage/home.html'), name = 'logout'),
    path('announcements/', include('announcements.urls')),
    path('notification/', include('notification.urls')),
    path('loggedin/', notify_views.loggedin, name='notifications'),
    path('notification/give_notification/<str:usrname>/', notify_views.give_notification, name='give-notification'),
    path('notification/give_notification/<str:usrname>/give/', notify_views.give),
    path('groups/', include('groups.urls')),
    path('post/', include('blogpost.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
