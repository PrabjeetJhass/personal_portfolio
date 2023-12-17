from django.urls import path
from .views import shortenUrl, index_view, redirectTo

urlpatterns = [
    path('', index_view, name='index'),
    path('shortenUrl/', shortenUrl, name='shortenUrl'),
    path('<str:shortUrl>/', redirectTo, name='redirect')
]