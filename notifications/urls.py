from django.urls import path
from .views import register_user, CustomLogin, send_notification
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", CustomLogin.as_view(), name="login"),
    path(
        "devices/",
        FCMDeviceAuthorizedViewSet.as_view({"post": "create"}),
        name="create_fcm_device",
    ),
    path("send-notification/", send_notification, name="send-notification"),
]
