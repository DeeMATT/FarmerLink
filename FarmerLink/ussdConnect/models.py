from django.db import models
from django.utils.timezone import now


class Users(models.Model):
    name = models.TextField(null=False)
    location = models.TextField(null=False)
    crops = models.TextField(null=False)
    userType = models.TextField(null=False)

    createdOn = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)
    lastActiveOn = models.DateTimeField(default=now)