from django.urls import path
from .views import register_lending, update_lending, update_lending_form, read_lending, read_lending_form, delete_lending

app_name = "Emprestimo"

urlpatterns = [
    path("register/lending", register_lending, name="register_lending"),
    path("update/lending", update_lending, name="update_lending"),
    path("update/lending/<str:pk>", update_lending_form,
         name="update_lending_form"),
    path("read/lending", read_lending, name="read_lending"),
    path("read/lending/<str:pk>", read_lending_form, name="read_lending_form"),
    path("delete/lending", delete_lending, name="delete_lending")
]
