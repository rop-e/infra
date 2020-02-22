from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    avata = models.ImageField(upload_to='imagens/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.user.username
