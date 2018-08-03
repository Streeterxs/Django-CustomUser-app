from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from authenticator.forms import SigningUping
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
# Create your views here.


def loginning (request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=raw_password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = AuthenticationForm()
    return render(request, 'authenticator/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SigningUping(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    else:
        form = SigningUping()

    return render(request, 'authenticator/signup.html', {'form': form})


def logingout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)