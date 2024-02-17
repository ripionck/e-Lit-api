from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publisher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(default='default.jpg', upload_to='publisher/images/')
    address = models.TextField()
    is_publisher = models.BooleanField(default=False)

    def __str__(self):
        return self.name
