from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateFormNone, ProfileUpdateFormStudent, ProfileUpdateFormProfessional, ProfileUpdateFormBoth
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


def profile_display_view(request):
    return render(request, "profile-display.html")

def get_user_profile(request, username):
    # print("HEY!!!!!!")
    user = User.objects.get(username=username)
    return render(request, 'profile-display.html', {"user":user})


def register(request):
    # if request.method =='POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Your account has been created! You are now able to log in')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
    # return render(request, 'register.html')



@login_required
def profile(request, parent_or_child=None, pk=None):
    # Get ID information of user
    thisUser = request.user.id
    same_user = ProfileUpdateFormNone.Meta.model.objects.values('user_id')
    all_users = ProfileUpdateFormNone.Meta.model.objects.values()

    for all in all_users:
        if all['student'] == True and all['professional'] == False:
            for same in same_user:
                same = int(same['user_id'])
                thisUser = int(thisUser)
                # Varifying ID is the same
                if same == thisUser and same == all['user_id']:
                    # generate page
                    if request.method =='POST':
                        u_form = UserUpdateForm(request.POST, instance=request.user)
                        p_form = ProfileUpdateFormStudent(request.POST, request.FILES, instance=request.user.profile)
                        if u_form.is_valid() and p_form.is_valid():
                            u_form.save()
                            p_form.save()
                            messages.success(request, f'Your account has been updated!')
                            return redirect('profile')
                    else:
                        u_form = UserUpdateForm(instance=request.user)
                        p_form = ProfileUpdateFormStudent(instance=request.user.profile)
                    context = {
                        'u_form': u_form,
                        'p_form': p_form
                    }
                    return render(request, 'profile.html', context)

        elif all['student'] == False and all['professional'] == True:
            for same in same_user:
                same = int(same['user_id'])
                thisUser = int(thisUser)
                # Varifying ID is the same
                if same == thisUser and same == all['user_id']:
                    # generate page
                    if request.method =='POST':
                        u_form = UserUpdateForm(request.POST, instance=request.user)
                        p_form = ProfileUpdateFormProfessional(request.POST, request.FILES, instance=request.user.profile)
                        if u_form.is_valid() and p_form.is_valid():
                            u_form.save()
                            p_form.save()
                            messages.success(request, f'Your account has been updated!')
                            return redirect('profile')
                    else:
                        u_form = UserUpdateForm(instance=request.user)
                        p_form = ProfileUpdateFormProfessional(instance=request.user.profile)
                    context = {
                        'u_form': u_form,
                        'p_form': p_form
                    }
                    return render(request, 'profile.html', context)

        elif all['student'] == True and all['professional'] == True:
            for same in same_user:
                same = int(same['user_id'])
                thisUser = int(thisUser)
                # Varifying ID is the same
                if same == thisUser and same == all['user_id']:
                    # generate page
                    if request.method =='POST':
                        u_form = UserUpdateForm(request.POST, instance=request.user)
                        p_form = ProfileUpdateFormBoth(request.POST, request.FILES, instance=request.user.profile)
                        if u_form.is_valid() and p_form.is_valid():
                            u_form.save()
                            p_form.save()
                            messages.success(request, f'Your account has been updated!')
                            return redirect('profile')
                    else:
                        u_form = UserUpdateForm(instance=request.user)
                        p_form = ProfileUpdateFormBoth(instance=request.user.profile)
                    context = {
                        'u_form': u_form,
                        'p_form': p_form
                    }
                    return render(request, 'profile.html', context)

        else:
            for same in same_user:
                same = int(same['user_id'])
                thisUser = int(thisUser)
                # Varifying ID is the same
                if same == thisUser and same == all['user_id']:
                    # generate page
                    if request.method =='POST':
                        u_form = UserUpdateForm(request.POST, instance=request.user)
                        p_form = ProfileUpdateFormNone(request.POST, request.FILES, instance=request.user.profile)
                        if u_form.is_valid() and p_form.is_valid():
                            u_form.save()
                            p_form.save()
                            messages.success(request, f'Your account has been updated!')
                            return redirect('profile')
                    else:
                        u_form = UserUpdateForm(instance=request.user)
                        p_form = ProfileUpdateFormNone(instance=request.user.profile)
                    context = {
                        'u_form': u_form,
                        'p_form': p_form
                    }
                    return render(request, 'profile.html', context)
