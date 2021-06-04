from django.db import models
from datetime import datetime
from flash_card_login_app.models import User


class State(models.Model):
    name = models.CharField('Name of State',max_length = 255)
    capital =  models.CharField("State's capital",max_length = 255)
    flag = models.ImageField(null=True, blank=True, upload_to="media/")
    shape = models.ImageField(null=True, blank=True, upload_to="media/")
    order_statehood = models.CharField('Order of Statehood',max_length = 3, null=True, blank=True,)
    date_of_entry = models.DateField('Entry Date', null=True, blank=True,)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class List(models.Model):
    item = models.CharField('ToDo Item',max_length = 255)
    completed =  models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name = "user_lists", on_delete=models.CASCADE)
    priority = models.IntegerField('Priority Number', default=0, blank=True,)
    idea_date = models.DateField('Born Date', null=True, blank=True,)
    due_date = models.DateField('Due Date', null=True, blank=True,)

    def __str__(self):
        return self.item


class Word(models.Model):
    word = models.CharField('Word',max_length = 10)

    def __str__(self):
        return self.word


class WordFive(models.Model):
    word = models.CharField('Word',max_length = 10)
    
    def __str__(self):
        return self.word


class WordSix(models.Model):
    word = models.CharField('Word',max_length = 10)

    def __str__(self):
        return self.word


class WordSeven(models.Model):
    word = models.CharField('Word',max_length = 10)

    def __str__(self):
        return self.word


class WordEight(models.Model):
    word = models.CharField('Word',max_length = 10)

    def __str__(self):
        return self.word