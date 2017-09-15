from django.db import models

# Create your models here.
# class BoyOrGirl(models.Model):
#     name = models.CharField(max_length=32, null=True)
#     age = models.IntegerField(null=True)
#     sex = models.IntegerField(choices=((1,'男生'),(2,'女生')))
class Girl(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
class Boy(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    B2G = models.ManyToManyField(Girl)
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    BOY = models.ForeignKey(Boy, null=True)
    GIRL = models.ForeignKey(Girl, null=True)

