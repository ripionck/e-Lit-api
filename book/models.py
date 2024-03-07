from django.db import models
from publisher.models import Publisher
from author.models import Author
from django.utils.text import slugify
import uuid

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date=models.DateField()
    cover = models.ImageField(default='default.jpg', upload_to='book/book_covers/')
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
        # Generate a slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Remove the associated image file when the object is deleted
        if self.cover:
            storage, path = self.cover.storage, self.cover.path
            storage.delete(path)

        super(Book, self).delete(*args, **kwargs)