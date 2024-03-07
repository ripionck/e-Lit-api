from django.db import models
import uuid

# Create your models here.
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True)
    biography = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='author/author_photos/')

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
    def delete(self, *args, **kwargs):
        # Remove the associated image file when the object is deleted
        if self.image:
            storage, path = self.image.storage, self.image.path
            storage.delete(path)

        super(Author, self).delete(*args, **kwargs)
