from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    minimum_experience = models.IntegerField(default=0)
    def __str__(self):
        return self.title
