from django.db import models
from django.db.models.fields import CharField, TextField, EmailField, IntegerField
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
    phone_number = models.IntegerField()

    def __str__(self):
        return str(self.flat_no)


class Notice(models.Model):
    header_notice = CharField(max_length=100)
    details_notice = TextField()

    def __str__(self):
        return self.header_notice

class Complaint(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    content = models.TextField()
    complaint_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.contact_name)

class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    staff_email = models.EmailField()
    staff_phone = models.IntegerField()
    designation = models.CharField(max_length=100)
    about = models.TextField(null=True)
    image = models.ImageField(upload_to='main/images')
    def __str__(self):
        return str(self.designation)
