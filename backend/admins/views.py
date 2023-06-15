from rest_framework import generics

from admins.models import Admins
from admins.serializers import AboutAdminsSerializers, AdminsSerializers, CreateAdminsSerializers
from testBackend.permissions import IsSuperAdmin


# Super
class AdminsViewList(generics.ListAPIView):
    queryset = Admins.objects.all()
    serializer_class = AboutAdminsSerializers
    permission_classes = [IsSuperAdmin]


# Super
class AdminsViewRetrieve(generics.RetrieveAPIView):
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializers
    permission_classes = [IsSuperAdmin]


# Super
class AdminsViewUpdate(generics.UpdateAPIView):
    queryset = Admins.objects.all()
    serializer_class = CreateAdminsSerializers
    permission_classes = [IsSuperAdmin]


# Super
class AdminsViewDestroy(generics.DestroyAPIView):
    queryset = Admins.objects.all()
    serializer_class = CreateAdminsSerializers
    permission_classes = [IsSuperAdmin]
