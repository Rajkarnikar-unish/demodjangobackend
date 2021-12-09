from rest_framework import fields, serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "title",
            "num_pages",
            "published_date",
            "price",
            "color",
            "isbn13",
        ]
        extra_kwargs = {
            "published_date": {"required": False},
            "price": {"required": False},
            "color": {"required": False},
            "isbn13": {"required": False},
        }
