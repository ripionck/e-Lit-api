from django.db import models
from publisher.models import Publisher
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    biography = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='author/images/')

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date=models.DateField()
    cover = models.ImageField(default='default.jpg', upload_to='book/covers/')
    isbn = models.CharField(max_length=13, unique=True)
    edition = models.CharField(max_length = 100)
    page_count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Ordering by creation date descending

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate slug if it's empty
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)