from django.db import models
from user.models import CustomUser
from book.models import Book

# Create your models here.
TRANSACTION_TYPE = (
    ("Deposite", "Deposite"),
    ("Purchase", "Purchase"),
)

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(choices=TRANSACTION_TYPE, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.amount = self.book.price * self.amount
        super().save(*args, *kwargs)