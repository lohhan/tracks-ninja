from django.db import models

# Create your models here.

class Track(models.Model):
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=20)
   artist = models.CharField(max_length=50)
   duration = models.FloatField()
   last_play = models.DateTimeField()

   def __str__(self):
      return self.title
