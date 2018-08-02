from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from authenticator.forms import SigningUping
from django.contrib.auth import login, authenticate

# Create your views here.


def loginning (request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('core:index')
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
            return redirect('core:index')

    else:
        form = SigningUping()

    return render(request, 'authenticator/signup.html', {'form': form})