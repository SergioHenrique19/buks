from django.urls import path
from .views import register_book, update_book, update_book_form

app_name = "Livros"

urlpatterns = [
    path("register/book", register_book, name="register_book"),
    path("update/book/", update_book, name="update_book"),
    path("update/book/<str:pk>/", update_book_form, name="update_book_form"),
]
