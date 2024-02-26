from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    date_of_death = serializers.DateField(required=False, allow_null=True)
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death', 'biography', 'image']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None