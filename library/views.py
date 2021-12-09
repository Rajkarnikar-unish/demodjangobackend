from django.db.models.query import QuerySet
from django.http import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookList(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class BookDetail(APIView):
    def get(self, request, pk):
        queryset = Book.objects.get(pk=pk)
        serializer = BookSerializer(queryset)
        return Response(serializer.data)


class PostBook(APIView):
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
