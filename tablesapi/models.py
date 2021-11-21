from django.db import models

class Pictures (models.Model):
    uid = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    thumbnailUrl = models.URLField(max_length=200)
    album = models.CharField(max_length=100)
    authorFirstName = models.CharField(max_length=50)
    authorLastName = models.CharField(max_length=50)
    authorUserName = models.CharField(max_length=50)




