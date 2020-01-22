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
