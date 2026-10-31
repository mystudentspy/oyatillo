from django.db.models import Q
from django.shortcuts import render
from django.views import View
from .models import Book, User, UserBook

class HomeView(View):
    def get(self, request):
        return render(
            request,
            "library/home.html"
        )

class BookView(View):
    def get(self, request):
        search = request.GET.get("search")
        if search:
            books = Book.objects.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search)
            )
        else:
            books = Book.objects.all()
        return render(
            request,
            "library/book_list.html",
            {
                "books": books,
                "search": search
            }
        )

class DetailBookView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(
            request,
            "library/detail_book.html",
            {
                "book": book
            }
        )



class UserView(View):
    def get(self, request):
        users = User.objects.all()
        return render(
            request,
            "library/user_list.html",
            {
                "users": users
            }
        )
class DetailUserView(View):
    def get(self, request, pk):
        user =User.objects.get(pk=pk)
        return render(
            request,
            "library/detail_user.html",
            {
                "user": user
            }
        )

class UserBookView(View):
    def get(self, request):
        userbooks = UserBook.objects.all()
        return render(
            request,
            "library/userbook_list.html",
            {
                "userbooks": userbooks
            }
        )
class DetailUserBookView(View):
    def get(self, request, pk):
        userbook = UserBook.objects.get(pk=pk)
        return render(
            request,
            "library/detail_userbook.html",
            {
                "userbook": userbook
            }
        )
