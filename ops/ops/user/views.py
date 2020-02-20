from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import UserInfo

# Create your views here.



def index(request):
    return render(request, 'index.html')


def login(username,password):
    try:
        person = UserInfo.objects.get(uname=username)
        try:
            person = UserInfo.objects.get(uname=username,userpwd=password)
            return 'login successfully'
        except:
            return 'Password not correct'
    except:
        return 'User not exits'


def register(username,password):
    try:
        person = UserInfo.objects.get(uname=username)
        return 'Account already exits'
    except:
        UserInfo(uname=username, userpwd=password).save()
        return 'Register successfully'



def login_regester(request):
    username = request.POST['username']
    password = request.POST['password']
    way = request.POST['way']
    if way == 'login':
        return HttpResponse(login(username, password))
    elif way == 'register':
        return HttpResponse(register(username, password))


# def dbtest(request):
#     result = ''
#     if request.method == 'POST' and request.POST:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         dbTest = UserInfo()
#         dbTest.uname = username
#         dbTest.userpwd = password
#         dbTest.save()
#         result = 'Success'
#
#     return render(request,'index.html', {'result':result})
