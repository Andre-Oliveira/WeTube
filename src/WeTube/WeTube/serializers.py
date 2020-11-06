from rest_framework import serializers
from django.contrib.auth.models import User
from Video.models import Video, VideoComment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'video_type', 'is_mature', 'pub_date', 
                    'votes_up', 'votes_down', 'description', 'path', 'user']