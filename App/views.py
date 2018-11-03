from django.shortcuts  import render
from .forms import Userform
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms

def registration(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email= email, password= password)
            return HttpResponseRedirect('/registration/')
    else:
        form = Userform()
    return render(request, 'registration.html', {'form':form})

class LoginForm(AuthenticationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password =  forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


def homepage_view(request):
    return render(request, 'home.html', {})