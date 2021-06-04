from django.db import models
from datetime import datetime
import re, bcrypt

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class UserManager(models.Manager):

    def register_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        if len(postData['password']) < 8:
            errors['password'] = "Password cannot be less than 8 characters."
        elif postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match."
        if len(postData['email']) < 1:
            errors['reg_email'] = "Email address cannot be blank."
        elif not EMAIL_REGEX.match(postData['email']):
            errors['reg_email'] = "Please enter a valid email address."
        elif check:
            errors['reg_email'] = "Email address is already registered."
        return errors

    def login_validator(self, postData):
        errors = {}
        check = User.objects.filter(username=postData['login_username'])
        if not check:
            errors['login_username'] = "Username has not been registered."
        else:
            if not bcrypt.checkpw(postData['login_password'].encode(), check[0].password.encode()):
                errors['login_username'] = "User ID and password do not match."
        return errors



class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 60)
    username = models.CharField(max_length = 255, null=True, blank=True)
    add_count =  models.IntegerField('Correct Addition', default=0, blank=True,)
    div_count =  models.IntegerField('Correct Dvision',default=0, blank=True,)
    multi_count = models.IntegerField('Correct Multiplication',default=0,blank=True)
    sub_count = models.IntegerField('Correct Subtraction', default=0,blank=True,)
    capital_count = models.IntegerField('Correct State capitals',default=0, blank=True,)
    flag_count = models.IntegerField('Correct State flags',default=0, blank=True,)
    shape_count = models.IntegerField('Correct State shapes',default=0, blank=True,)
    word_scram_count = models.IntegerField('Correct Word Scrambler',default=0, blank=True,)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

    def __str__(self):
        return self.username 