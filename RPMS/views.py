from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import contact_info, UserProfile
from .forms import FileUploadForm
from .models import UploadedFile     

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
            d = request.POST.get('name')
            e = request.POST.get('department')
            f = request.POST.get('position')
            g = request.POST.get('education')
            h = request.POST.get('research_interests')
            i = request.FILES['profile_photo']
            if b==c:
                #Check whether user name is unique
                if (User.objects.filter(username = a)):
                    return render(request, 'RPMS/registration.html', {'error':'Username Already Exists Try again with different username'})
                else:
                    user = User.objects.create_user(username = a, password=b)
                    user.save()
                    usrp = UserProfile(user=user,name=d,department=e,position=f,education=g,research_interests=h, profile_photo=i)
                    usrp.save()
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

def contact(request):
    # return HttpResponse('<h1>this is the contact page</h1>')
    if request.method == 'GET':
        return render(request, 'RPMS/contact.html')
    elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        print(email)
        print(message)
        return render(request,'RPMS/contact.html',{'feedback':'Your message has been recorded'})
    
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user) 
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'RPMS/profile.html', {'uploaded_files': uploaded_files, 'user': user, 'profile': profile})


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('profile')
    else:
        form = FileUploadForm()
    return render(request, 'RPMS/upload_file.html', {'form': form})




