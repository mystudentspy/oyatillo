from .models import User, Book, UserBook
from import_export import admin as ie_admin
from django.contrib import admin

@admin.register(Book)
class BookAdmin(ie_admin.ImportExportModelAdmin):
    list_display = ('title', 'author',)

@admin.register(User)
class UserAdmin(ie_admin.ImportExportActionModelAdmin):
    list_display = ('role', 'first_name', 'last_name',)

@admin.register(UserBook)
class UserBookAdmin(ie_admin.ImportExportModelAdmin):
    list_display = ('user', 'book', 'olindi')

