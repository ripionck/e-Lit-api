from django.contrib import admin
from django.utils.text import slugify
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'price', 'slug')
    search_fields = ('title', 'author')
    list_filter = ('author', 'publication_date')
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        # Automatically generate slug if it's empty
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)

