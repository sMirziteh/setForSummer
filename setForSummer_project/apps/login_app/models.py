from django.db import models
# from ..wall_app.models import Messages, Comments
import re
import bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^(([A-za-z]+[\s]{1}[A-za-z]+)|([A-Za-z]+))$')


class UsersManager(models.Manager):
    def validateRegistration(self, postData):
        # validateRegistration
        errors = []
        if not NAME_REGEX.match(postData['first_name']):
            errors.append('invalid name entry')
        if not NAME_REGEX.match(postData['last_name']):
            errors.append('invalid name entry')
        if len(postData['first_name']) < 1 or len(postData['last_name']) < 1:
            errors.append('Must enter name')
        if len(postData['first_name']) > 15 or len(postData['last_name']) > 15:
            errors.append('Name must be shorter than 15 characters')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('invalid email entry')
        if len(Users.objects.filter(email=postData['email'])):
            errors.append('User already exists')
        if postData['pw'] != postData['cpw']:
            errors.append('passwords do not match')
        if len(postData['pw']) < 6:
            errors.append('Password must be longer than 6 characters')
        if len(errors):
            return errors
        user = Users.objects.create(
            first_name=postData['first_name'],
            last_name=postData['last_name'],
            email=postData['email'],
            pwd=bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
        )
        return user

    def validateLogin(self, postData):
        user_list = Users.objects.filter(email=postData['lemail'])
        if len(user_list):
            if bcrypt.checkpw(postData['lpassword'].encode(), user_list[0].pwd.encode()):
                print("passwords match")
                return user_list[0]
        return 'invalid email / password combination'
            


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    objects = UsersManager()

    def __repr__(self):
        return f"<User: {self.first_name} {self.last_name} {self.email} {self.pwd}>"
