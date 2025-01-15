from django.db import models

#custom user model
class RigisterdUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone  = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    address2 = models.TextField()

    def __str__(self):
        return self.username