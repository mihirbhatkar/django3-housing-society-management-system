from django.db import models
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User

class MainPage(models.Model):
    society_name = CharField(max_length=200)
    society_about = TextField()

    def __str__(self):
        return self.society_name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField()
    age = models.IntegerField(blank=True)
    flat_no = models.CharField(max_length=10)
    phone_number = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.flat_no)


class Notice(models.Model):
    header_notice = CharField(max_length=100)
    details_notice = TextField()

    def __str__(self):
        return self.header_notice
