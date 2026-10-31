from django.urls import path
from .views import (
    HomeView,
    BookView,
    UserView,
    UserBookView
)
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books', BookView.as_view(), name='books'),
    path('users/', UserView.as_view(), name='users'),
    path('userbooks/', UserBookView.as_view(), name='userbooks'),
]
