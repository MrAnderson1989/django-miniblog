from django.db import models

# Create your models here.


# class Item(models.Model):
#     id = models.IntegerField(primary_key=True)
#     text = models.CharField(max_length=20)


class post(models.Model):
    title = models.CharField(u'文章标题',max_length=50)
    author = models.CharField(u'作者',max_length=20)
    content = models.TextField(u'内容',max_length=2000)



