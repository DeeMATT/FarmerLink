from django.db import models
from django.utils.timezone import now


class Users(models.Model):
    name = models.TextField(null=False)
    location = models.TextField(null=False)
    crops = models.TextField(null=False)
    userType = models.TextField(null=False)
    phoneNumber = models.IntegerField(null=False, default=0)
    userId = models.IntegerField(null=False, default=0)

    createdOn = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)
    lastActiveOn = models.DateTimeField(default=now)


class CropOrders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    location = models.TextField(null=False)
    crop = models.TextField(null=False)
    QuantityInNumber = models.TextField(null=True)

    entryId = models.TextField(null=False)
    createdOn = models.DateTimeField(auto_now_add=True)


class CropAvailability(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    sex = models.TextField(null=False)
    crop = models.TextField(null=False)
    location = models.TextField(null=False)
    unitOfMeasure = models.TextField(null=False)
    QuantityInNumber = models.TextField(null=True)
    
    entryId = models.TextField(null=False)
    createdOn = models.DateTimeField(auto_now_add=True)

