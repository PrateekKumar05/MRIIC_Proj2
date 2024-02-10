from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'RPMS/home.html')
    # return HttpResponse('Home Page')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'RPMS/loginuser.html', {'form':AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username=a, password=b)
        if user is None:
            return render(request,'RPMS/loginuser.html', {'form':AuthenticationForm(), 'error':'Invalid Credentials'})
        else:
            login(request, user)
            return redirect('home')


def registration(request):
        if request.method == 'GET':
            return render(request, 'RPMS/registration.html', {'form':UserCreationForm()})
        else:
            a = request.POST.get('username')
            b = request.POST.get('password1')
            c = request.POST.get('password2')
            if b==c:
                #Check whether user name is unique
                if (User.objects.filter(username = a)):
                    return render(request, 'RPMS/registration.html', {'error':'Username Already Exists Try again with different username'})
                else:
                    user = User.objects.create_user(username = a, password=b)
                    user.save()
                    login(request,user)
                    return redirect('home')
            else:
                return render(request, 'RPMS/registration.html', {'form':UserCreationForm(), 'error':'Password Mismatch Try Again'})
        
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')
    
def aboutus(request):
    return render(request, 'RPMS/aboutus.html')