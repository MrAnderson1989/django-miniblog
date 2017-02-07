from django.contrib import admin
from .models import article
from .models import Post


# Register your models here.

admin.site.register(article)

admin.site.register(Post)

