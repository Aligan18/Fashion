from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from comments.models import Comments
from comments.serializers import CommentsSerializers, CreateCommentsSerializers, AboutCommentsSerializers
from comments.service import CommentsFilter
from testBackend.permissions import IsOwner, IsClient


# Admin,  Client после покупки
class CommentsAPICreate(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CreateCommentsSerializers
    permission_classes = [IsAdminUser | IsClient]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()



#########################################################################
# All
class CommentsAPIListAll(generics.ListAPIView):  # Все коментарии продукта
    queryset = Comments.objects.all()
    serializer_class = AboutCommentsSerializers
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CommentsFilter


#########################################################################


# Admin,  Client автор
class CommentsAPIDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CreateCommentsSerializers
    permission_classes = [IsAdminUser | IsOwner]
