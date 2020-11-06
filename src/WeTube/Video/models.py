from django.db import models

# Create your models here.
class Video(models.Model):
    CHOICES = [
        ('MUSICVIDEO', 'Music Video'),
        ('DOCUMENTARY', 'Documentary'),
        ('NEWS', 'News'),
        ('ENTERTAINMENT', 'Entertainement'),
    ]
    title = models.CharField(max_length=200)
    video_type = CHOICES
    is_mature = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True, blank=False, null=False)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True, blank=False, null=False)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)