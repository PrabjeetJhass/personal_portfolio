from django.urls import path
from .views import index_view

urlpatterns = [
    path('notify/', index_view, name='index_view')
]