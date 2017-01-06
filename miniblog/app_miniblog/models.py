from django.db import models

# Create your models here.


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=20)


class post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    Author = models.CharField(max_length=20)
    date = models.DateTimeField()
    content = models.CharField(max_length=2000)

