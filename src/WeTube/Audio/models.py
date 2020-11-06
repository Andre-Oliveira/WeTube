from django.db import models

# Create your models here.

class Audio(models.Model):
    CHOICES = [
        ('MUSIC', 'Music'),
        ('PODCAST', 'Podcast'),
        ('AUDIOBOOK', 'Audio Book'),
    ]
    title = models.CharField(max_length=200)
    audio_type = CHOICES
    is_mature = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True, blank=False, null=False)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
class AudioComment(models.Model):
    comment_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True, blank=False, null=False)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)