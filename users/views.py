from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy


def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
