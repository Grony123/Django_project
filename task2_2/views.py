from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Details
from django.contrib.auth.models import User

def home(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            fname = request.POST['name1']
            lname = request.POST['name2']
            phone = request.POST['mob']
            email = request.POST['email']
            password = request.POST['password1']
            try:
                user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email )
                details = Details(user=user, phone_no= phone)
                details.save()
                return redirect('success')
            except:
                messages.error(request,f'User already exist')
                return render(request,'task2_2/signup.html',)
        else:
            messages.error(request, f'Passwords do not match :)')
            return render(request,'task2_2/signup.html',)
    return render(request,'task2_2/signup.html')

def log_in(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('success')
            else:
                messages.error(request,f'Invalid Credentials')
                return render(request,'task2_2/signin.html',)
    return render(request,'task2_2/signin.html',)


def log_out(request):
    logout(request)
    messages.success(request,f'Successfully Logged out!')
    return render(request,'task2_2/signup.html',)

def success(request):
    details = Details.objects.get(user=request.user)
    return render(request,'task2_2/success.html',{'data':details})