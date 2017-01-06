from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth

# Create your views here.
def home(request):
    # return HttpResponse('hello world')
    return render(request,'home.html')

def post(request):
    if request.method == 'GET':
        return render(request,'post.html')
    if request.method == 'PUT':
        pass #修改文章
    if request.method == 'POST':
        pass #添加文章
    if request.method == 'DELETE':
        pass #删除

def login(request):
    if request.method=='POST':
        pass
        if request.POST['username']!=None and request.POST['password']!=None:
            pass
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user= auth.authenticate(username=username,password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/dashboard")
            else:
                return render(request,'login.html',{'alert':'alert-danger','display':'block','msg':'用户名或密码错误！'})
        else:
            # <div class="alert alert-danger" role="alert">...</div>
            return render(request,'login.html',{'alert':'alert-danger','display':'block','msg':'用户名或密码不能为空！'})
    else:
        return render(request,'login.html',{'alert':'alert-danger','display':'none','msg':'用户名或密码不能为空！'})

def dashboard(request):
    if request.user.is_authenticated():
        return render(request,'dashboard.html')
    else:
        return HttpResponseRedirect("/login")

def updaload(request):
    pass


