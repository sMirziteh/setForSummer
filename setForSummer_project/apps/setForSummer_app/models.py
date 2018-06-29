from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserSignupManager(models.Manager):
    def signupform(self, postData):
        
        result = Users.objects.create(
            user_name = postData['name'],
            email = postData['email'],
            phone = postData['phone'],
            zipcode = postData['zip'],
            relationship = postData['relationship']
        ) 

        if 'newsletter' in postData:
            result.newsletter = True
        if 'food' in postData:
            result.food = True
        if 'activities' in postData:
            result.activities = True
        if 'learning' in postData:
            result.learning = True
        result.save()
        
        print("models side result:", result)
        return result

class Users(models.Model):
    user_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=5)
    relationship = models.CharField(max_length = 255)
    newsletter = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    activities = models.BooleanField(default=False)
    learning = models.BooleanField(default=False)
    objects = UserSignupManager()
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