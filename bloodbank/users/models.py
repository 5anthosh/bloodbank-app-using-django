from django.db import models
from django.contrib.auth.models import User, AbstractUser


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
# Create your models here.


#class CustomUser(AbstractUser):
 #   pass