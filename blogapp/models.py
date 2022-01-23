from distutils.command.upload import upload
from pickle import TRUE
from tokenize import blank_re
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="appImage",blank=TRUE)
    body = models.TextField()

    def __str__(self):
        return self.title
     
