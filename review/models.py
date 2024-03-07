from django.db import models
from django.contrib.auth.models import User
from book.models import Book
import uuid

# Create your models here.
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'book']  # Each user can review each book only once

    def __str__(self):
        return f'{self.user.username}\'s review for {self.book.title}'