from django.conf.urls import url
from django.urls import path
from notification import views as notify_views

urlpatterns = [
 path('show/<int:notification_id>/', notify_views.show_notification),
 path('delete/<int:notification_id>/', notify_views.delete_notification),

]
