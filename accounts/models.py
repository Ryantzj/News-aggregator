from django.db import models

# Create your models here.

class Account(models.Model):
	userID = models.CharField(max_length=2)
	username = models.CharField(max_length=10)
	password = models.CharField(max_length=10)
	deleted = models.CharField(max_length=20)
	permission = models.CharField(max_length=2)

