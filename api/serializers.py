from rest_framework import serializers
from home.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'nickname', 'favourite_keyboards')