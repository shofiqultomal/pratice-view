from django.db import models

# Create your models here.
class Members(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
