from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error': 'User already exists with the same username'})
            except User.DoesNotExist:
                # Create the user inside the try block
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                # Log in the user
                auth.login(request, user)
                return redirect('login')
        else:
            return render(request, 'account/signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'Username or Password is incorrect.'})
    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'account/signup.html')
