from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'book', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'book']  # These fields are automatically set, so they should be read-only
