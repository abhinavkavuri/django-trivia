from django.db import models


# Create your models here.
class Scores(models.Model):
    user_name = models.CharField(max_length=40, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()



