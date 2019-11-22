from django.urls import path
from .views import register_book

app_name = "Livros"

urlpatterns = [
    path("register/book", register_book, name="register_book"),
]
