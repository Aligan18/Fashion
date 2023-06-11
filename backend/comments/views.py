from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from comments.models import Comments
from comments.serializers import CommentsSerializers


# Admin,  Client после покупки
class CommentsAPICreate(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers


# All
class CommentsAPIListAll(generics.ListAPIView):  # Все коментарии продукта
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers


# Admin,  Client автор
class CommentsAPIDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers

