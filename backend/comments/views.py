from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from comments.models import Comments
from comments.serializers import CommentsSerializers, CreateCommentsSerializers, AboutCommentsSerializers
from testBackend.permissions import IsOwner, IsClient


# Admin,  Client после покупки
class CommentsAPICreate(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CreateCommentsSerializers
    permission_classes = [IsAdminUser | IsClient]


#########################################################################
# All
class CommentsAPIListAll(generics.ListAPIView):  # Все коментарии продукта
    queryset = Comments.objects.all()
    serializer_class = AboutCommentsSerializers
    permission_classes = [AllowAny]
#########################################################################


# Admin,  Client автор
class CommentsAPIDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CreateCommentsSerializers
    permission_classes = [IsAdminUser | IsOwner]


