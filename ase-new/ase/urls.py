from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from notification import views as notify_views
from rating import views as rate_views
from friends import views as friend_views

urlpatterns = [
    path('', include('homepage.urls')),
    path('dashboard/', include('userapp.urls')),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('signin/', auth_views.LoginView.as_view(template_name='homepage/signin.html'), name = 'signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage/home.html'), name = 'logout'),
    path('announcements/', include('announcements.urls')),
    path('notification/', include('notification.urls')),
    path('loggedin_p/', notify_views.loggedin_p, name='notifications'),
    path('loggedin_i/', notify_views.loggedin_i, name='notifications'),
    path('loggedin_g/', notify_views.loggedin_g, name='notifications'),
    path('loggedin_a/', notify_views.loggedin_a, name='notifications'),
    path('shared_items/<int:id>/', notify_views.shared_items, name="shared-items"),
    path('borrowed_items/<int:id>/', notify_views.borrowed_items, name="borrowed-items"),
    path('notification/give_i_notification/<str:usrname>/', notify_views.give_i_notification, name='give-item-notification'),
    path('notification/give_i_notification/<str:usrname>/give_i/', notify_views.give_i),
    path('notification/give_p_notification/<str:usrname>/', notify_views.give_p_notification, name='give-personal-notification'),
    path('notification/give_p_notification/<str:usrname>/give_p/', notify_views.give_p),
    path('groups/', include('groups.urls')),
    path('give_rating/<str:usrname>/', rate_views.give_rating, name='give-rating'),
    path('give_rating/<str:usrname>/rate/', rate_views.rate),
    path('leaderboard/', rate_views.leaderboard, name='leaderboard'),
    path('give_report/<str:usrname>/', rate_views.give_report, name='give-report'),
    path('give_report/<str:usrname>/report/', rate_views.report),
    path('friends/', friend_views.friends, name='friends'),
    path('user_profile/<str:usrname>/', friend_views.user_profile, name='user-profile'),
    path('leaderboard/user_profile/<str:usrname>/', friend_views.user_profile, name='user-profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
