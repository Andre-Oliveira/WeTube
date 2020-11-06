from rest_framework import serializers
from django.contrib.auth.models import User
from Video.models import Video, VideoComment
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'video_type', 'is_mature', 'pub_date', 
                    'votes_up', 'votes_down', 'description', 'path', 'user']