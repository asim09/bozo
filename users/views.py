from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm
from django.contrib import messages
from inventory.views import cab_view

# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('cab_view')
    else:
        form = UserSignUpForm()
        context = {'form':form}
        if request.method == 'POST':
            form = UserSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                print(user)
                messages.success(request, 'Account created for '+ user)
                return redirect('login')

        return render(request,'users/signup.html',context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('cab_view')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('cab_view')
            else:
                messages.info(request,'Username or ped is incorrect')

        return render(request,'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')

