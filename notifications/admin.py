from django.contrib import admin
from notifications.models import Notification, NotificationCount, FirebaseDeviceToken

admin.site.add(Notification)
admin.site.add(NotificationCount)
admin.site.add(FirebaseDeviceToken)
