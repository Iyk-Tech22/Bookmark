from django.db import models
from django.conf import settings


# PROFILE MODEL
class Profile(models.Model):
    """ Generate the profile model """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="user/%Y/%m/%d", blank=True)

    def __str__(self):
        return f" Profile of {self.user.username} "