from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='account/images/')
    phone = models.CharField(max_length=12)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'