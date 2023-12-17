from django.urls import path
from .consumers import Notify_consumer

websocket_urlpatterns = [
    path('ws/notify/', Notify_consumer.as_asgi()),
]
