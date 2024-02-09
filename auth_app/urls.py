from django.urls import path
from .views import sighup_view, signin_view, logout_view

urlpatterns = [
    path('suv/', sighup_view, name='signup_url'),
    path('siv/', signin_view, name='signin_url'),
    path('sio/', logout_view, name='logout_url')
]
