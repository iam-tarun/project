from django.conf.urls import url
from django.urls import path
from notification import views as notify_views
from friends import views as friend_views

urlpatterns = [
 path('shared_items/<int:id>/',notify_views.shared_items),
 path('borrowed_items/<int:id>/',notify_views.borrowed_items),
 path('show_f/<int:notification_id>/', friend_views.show_friend_request),
 path('show_p/<int:notification_id>/', notify_views.show_personal_notification),
 path('show_i/<int:notification_id>/', notify_views.show_image_notification),
 path('show_g/<int:notification_id>/',notify_views.show_group_notification),
 path('delete/<int:notification_id>/', notify_views.delete_notification),
]
