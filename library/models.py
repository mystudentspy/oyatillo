from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Book(TimeStampedModel):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        unique_together = ('title', 'author')

class User(TimeStampedModel):
    roles = (
        ("student", "Student"),
        ("teacher", "Teacher"),
    )
    role = models.CharField(default="Student", max_length=100, choices=roles)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UserBook(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    olindi = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.first_name} - {self.book.title}"
