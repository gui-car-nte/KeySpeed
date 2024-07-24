from rest_framework import viewsets, permissions
from home.models import UserProfile
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]