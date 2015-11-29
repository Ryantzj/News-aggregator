from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
	user = models.ForeignKey(User)
	postID = models.CharField(max_length=2)
	title = models.CharField(max_length=50)
	postContent = models.CharField(max_length=50)
	rankingPoints = models.IntegerField(default=0)
	createdDate = models.DateTimeField(auto_now_add=True)
	deleted = models.CharField(max_length=2)

class Comment(models.Model):
	user = models.ForeignKey(User)
	commentID = models.CharField(max_length=2)
	commentContent = models.CharField(max_length=50)
	createdDate = models.DateTimeField(auto_now_add=True)
	deleted = models.CharField(max_length=2)
