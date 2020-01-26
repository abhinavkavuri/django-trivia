from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)
    user_points = models.IntegerField(null=True)

    def __str__(self):
        return self.user_type


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.user_name} Profile'


"""
Type 0 - True/False
Type 1 - Multiple Choice questions
Type 2 - Essay type
"""


class Questions(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='DEFAULT AUTHOR', )
    question = models.TextField()
    question_type = models.CharField(max_length=20)
    op1 = models.CharField(max_length=100, null=True, blank=True)
    op2 = models.CharField(max_length=100, null=True, blank=True)  # --> Front-end check in-place
    op3 = models.CharField(max_length=100, null=True, blank=True)
    op4 = models.CharField(max_length=100, null=True, blank=True)  # --> Essay type Questions have no Answers and Options
    ans = models.CharField(max_length=100, null=True, blank=True)
    weightage = models.IntegerField()

    def __str__(self):
        return self.question


class Scores(models.Model):
    user_name = models.CharField(max_length=40, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
