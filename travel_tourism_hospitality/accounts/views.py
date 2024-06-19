from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        re_password = request.POST['re_pass']

        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Account has been created successfully. Countinue to Log in')
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'passwords not matching')
            return redirect('register')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect ('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
