from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='account/images/')
    phone = models.CharField(max_length=12)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_publisher = models.BooleanField(default=False)

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def __str__(self):
        return self.get_full_name()