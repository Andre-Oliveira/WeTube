from rest_framework import serializers
from django.contrib.auth.models import User
from Video.models import Video, VideoComment

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'video_type', 'is_mature', 
                    'description', 'path', 'user']