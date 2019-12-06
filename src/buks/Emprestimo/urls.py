from django.urls import path
from .views import register_lending

app_name = "Emprestimo"

urlpatterns = [
    path("register/lending", register_lending, name="register_lending"),
]
