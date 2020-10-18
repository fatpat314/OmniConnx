from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'student', 'professional']
        test = True
        student = model.objects.values('user')
        # print(model.objects.values())
        # print (list(model.objects.get('user_id')))

class ProfileUpdateFormStudent(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'student', 'professional', 'test']
        test = True
        student = model.objects.values('user_id')
        # print(model.objects.values())
        # print (list(model.objects.get('user_id')))

class ProfileUpdateFormProfessional(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'student', 'professional', 'test']
        test = True
        student = model.objects.values('user_id')
        # print(model.objects.values())
        # print (list(model.objects.get('user_id')))
