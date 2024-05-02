from django.db import models
from django.contrib.auth.models import User, AbstractUser


"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    nickname = models.CharField(max_length=10, null= True)
    image = models.ImageField(upload_to='profile/', null=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.nickname
"""

class Profile(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, null=True)
    nickname = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='profile/', null=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.nickname or str(self.username)
