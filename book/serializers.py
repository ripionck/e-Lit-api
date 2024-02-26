from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['slug']

    def get_image_url(self, obj):
        if obj.cover:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.cover.url)
        return None