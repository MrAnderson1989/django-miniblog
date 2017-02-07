from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    post_list = Post.objects.filter(status='published')
    return render(request,'home.html',{'list':post_list})


