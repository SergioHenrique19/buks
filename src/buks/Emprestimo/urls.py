from django.urls import path
from .views import register_lending, update_lending, update_lending_form

app_name = "Emprestimo"

urlpatterns = [
    path("register/lending", register_lending, name="register_lending"),
    path("update/lending", update_lending, name="update_lending"),
    path("update/lending/<str:pk>", update_lending_form, name="update_lending_form")
]
