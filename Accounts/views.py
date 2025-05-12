from django.shortcuts import render, redirect
from .forms import RegisterForm
from .utils import get_otp
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def registerview(request):
    fm = RegisterForm()  
    context = {
        'registerform': fm
    }

    if request.method == 'POST':
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save()  
            username = user.cleaned_data['username']
            email = user.cleaned_data['email']

            send_mail(
                'Registration Successful',
                f'{username}, You have successfully created an account in BookyourShow.',
                'suryareddy6969@gmail.com', 
                [email],
                fail_silently=True
            )
            return redirect('signin')  
    return render(request, 'Accounts/register.html', context)

def LoginView(request):
    if request.method == 'POST':
        fm = LoginForm(data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login form submission.")
        context = {'LoginForm': fm}
    else:
        context = {'LoginForm': LoginForm()}

    return render(request, 'Accounts/login.html', context)



def logoutview(request):
    logout(request)
    messages.success(request,f'you have been logged out') 
    return redirect('signin')   

@login_required(login_url='signin') 

def home(request):
    return render(request, 'Accounts/home.html')  

