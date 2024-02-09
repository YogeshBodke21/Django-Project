from django.urls import path
from .views import form_view, lap_retrieve_view, lap_delete_view, lap_update_view

urlpatterns = [
    path('lv/', form_view, name='add_url'),
    path('lr/', lap_retrieve_view, name= 'retrieve_url'),
    path('lru/<int:pk>/', lap_delete_view, name='delete_url'),
    path('lrv/<int:pk>/', lap_update_view, name='update_url')
]
