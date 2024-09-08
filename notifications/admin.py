from django.contrib import admin
from notifications.models import Notification, NotificationCount, FirebaseDeviceToken

admin.site.register(Notification)
admin.site.register(NotificationCount)
admin.site.register(FirebaseDeviceToken)
