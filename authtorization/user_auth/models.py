from django.db import models


class Users(models.Model):
    firstName = models.CharField(max_length=32)
    secondName = models.CharField(max_length=64)
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.mail
