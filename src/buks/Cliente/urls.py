from django.urls import path
from .views import register_client, update_client, update_client_form, read_client, read_client_form

app_name = "Cliente"

urlpatterns = [
    path('register/client', register_client, name="register_client"),
    path('update/client', update_client, name="update_client"),
    path('update/client/<str:pk>', update_client_form, name="update_client_form"),
    path('read/client', read_client, name="read_client"),
    path('read/client/<str:pk>', read_client_form, name="read_client_form"),
]
