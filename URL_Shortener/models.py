from django.db import models

class ShortenedLink(models.Model):
    shortUrl = models.CharField(max_length=255)
    longUrl = models.URLField()