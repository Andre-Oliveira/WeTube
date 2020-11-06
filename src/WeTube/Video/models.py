from django.db import models

# Create your models here.
class Video(models.Model):
    video = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.CharField(max_length=200)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)

class Comment(models.Model):
    user = models.CharField(max_length=200)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)