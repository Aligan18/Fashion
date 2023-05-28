from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from comments.models import Comments
from comments.serializers import CommentsSerializers


class CommentsAPIListAll(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers


class CommentsAPICreate(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers


class CommentsAPIDelete(generics.DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
