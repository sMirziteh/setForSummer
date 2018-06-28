from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=5)
    newsletter = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    activities = models.BooleanField(default=False)
    learning = models.BooleanField(default=False)
    relationship = models.CharField(max_length = 255)

    def __repr__(self):
        return f"<<Users: {self.user_name} {self.email} {self.phone} {self.zipcode} {self.newsletter} {self.food} {self.activities} {self.learning} {self.relationship}"




class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager()