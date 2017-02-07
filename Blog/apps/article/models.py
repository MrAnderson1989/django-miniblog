from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class article(models.Model):
    title = models.CharField(u'文章标题',max_length=30)
    author = models.CharField(u'作者',max_length=20)
    content = models.TextField(u'内容',max_length=2000)
    add_date = models.DateField(u'添加时间',auto_now_add=True)
    mod_date = models.DateField(u'修改时间',auto_now=True)

    def __str__(self):
        return self.title



class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(u'文章标题',max_length=250)
    slug = models.SlugField(u'链接',max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField(u'内容')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(u'添加时间',auto_now_add=True)
    updated = models.DateTimeField(u'修改时间',auto_now=True)
    status = models.CharField(u'状态',max_length=10,
    choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

# class Link(models.Model):

