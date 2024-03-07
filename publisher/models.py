from django.db import models
from account.models import CustomUser
import uuid

# Create your models here.
class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    logo = models.ImageField(default='default.jpg', upload_to='publisher/images/')
    address = models.TextField()

    def __str__(self):
        return self.name
