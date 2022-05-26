from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128)
    overview = models.TextField()
    poster_path = models.CharField(max_length=128)
    release_date = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

