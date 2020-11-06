from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Video(models.Model):
    class VideoType(models.TextChoices):
        MUSICVIDEO = 'Music Video', _('Music Video')
        DOCUMENTARY = 'Documentary', _('Documentary')
        NEWS = 'News', _('News')
        ENTERTAINMENT = 'Entertainement', _('Entertainement')
        UNSPECIFIED = 'Unspecified', _('Unspecified')
    video_type = models.CharField(
        max_length=14,
        choices=VideoType.choices,
        default=VideoType.UNSPECIFIED,
    )
    title = models.CharField(max_length=200)
    is_mature = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True, blank=False, null=False)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class VideoComment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True, blank=False, null=False)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)