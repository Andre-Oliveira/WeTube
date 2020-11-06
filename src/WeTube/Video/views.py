from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import VideoSerializer
from .models import Video

# Create your views here.
def index(request):
    return HttpResponse("Hello, there. You're at the Main Video page.")

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer