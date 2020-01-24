from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=25)
    user_type = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=70)
    user_points = models.IntegerField()

    def __str__(self):
        return self.user_name


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
    quiz_id = models.CharField(max_length=40, null=True)
    question = models.TextField(null=True)
    question_type = models.IntegerField(null=True)
    op1 = models.CharField(max_length=40, null=True)
    op2 = models.CharField(max_length=40, null=True)
    op3 = models.CharField(max_length=40, null=True)
    op4 = models.CharField(max_length=40, null=True)
    ans = models.CharField(max_length=40, null=True)
    weightage = models.IntegerField(null=True)

    def __str__(self):
        return self.question


class Scores(models.Model):
    user_name = models.CharField(max_length=40, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
