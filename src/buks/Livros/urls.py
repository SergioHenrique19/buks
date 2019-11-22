from django.urls import path
from .views import register_book, update_book, update_book_form, read_book, read_book_form, delete_book

app_name = "Livros"

urlpatterns = [
    path("register/book", register_book, name="register_book"),
    path("update/book/", update_book, name="update_book"),
    path("update/book/<str:pk>/", update_book_form, name="update_book_form"),
    path("read/book/", read_book, name="read_book"),
    path("read/book/<str:pk>/", read_book_form, name="read_book_form"),
    path("delete/book/", delete_book, name="delete_book"),
]
