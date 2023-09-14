from ..models import User
from rest_framework import status, generics
from .serializer import UserSerializer


class UserCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'name'

    def get_queryset(self):
        name = self.kwargs['name']
        return User.objects.filter(name=name)