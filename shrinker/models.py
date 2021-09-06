from shrinker.utilities import generate_short_url
from django.db import models

# Create your models here.
class ShortURL(models.Model):
  short_url = models.CharField(max_length=7, primary_key=True, default=generate_short_url)
  long_url = models.CharField(max_length=200)
  date_created = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.short_url