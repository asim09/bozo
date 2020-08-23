from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm
from django.contrib import messages
from inventory.views import cab_view
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group

from users.models import Customer

# Create your views here.

@unauthenticated_user
def signup(request):
    form = UserSignUpForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )
            messages.success(request, 'Account created for '+ username)
            return redirect('user_login')

    return render(request,'users/signup.html',context)

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or pwd is incorrect')

    return render(request,'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')

