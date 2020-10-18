from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileUpdateFormStudent, ProfileUpdateFormProfessional
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
def profile(request, parent_or_child=None, pk=None):

    thisUser = request.user.id
    # print("THIS USER: ", thisUser)
    # print("SAME: ", ProfileUpdateForm.Meta.model.objects.values('user_id'))
    same_user = ProfileUpdateForm.Meta.model.objects.values('user_id')
    all_users = ProfileUpdateForm.Meta.model.objects.values()

    # Match the current user with the object id
    for same in same_user:
        same = int(same['user_id'])
        thisUser = int(thisUser)
        # print("SAME: ", same)
        # Loop through all user objects
        for all in all_users:
            # verify the user id
            if thisUser == same:
                # Conditional
                if all['student'] == True:
                    # print('SUCCESS')
                    # Generate the student form
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
                else:
                    pass

                if all['professional'] == True:
                    # print('SUCCESS')
                    # Generate the student form
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
                else:
                    pass





            if all['student'] == False and all['professional'] == False:
                if request.method =='POST':
                    u_form = UserUpdateForm(request.POST, instance=request.user)
                    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
                    if u_form.is_valid() and p_form.is_valid():
                        u_form.save()
                        p_form.save()
                        messages.success(request, f'Your account has been updated!')
                        return redirect('profile')
                else:
                    u_form = UserUpdateForm(instance=request.user)
                    p_form = ProfileUpdateForm(instance=request.user.profile)
                context = {
                    'u_form': u_form,
                    'p_form': p_form
                }

                return render(request, 'profile.html', context)



    # if request.method =='POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    #
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile')
    #
    #     else:
    #         u_form = UserUpdateForm(instance=request.user)
    #         p_form = ProfileUpdateForm(instance=request.user.profile)
    #     context = {
    #         'u_form': u_form,
    #         'p_form': p_form
    #         }
    #
    #
    #     return render(request, 'profile.html', context)


                # elif all['student'] == False:

                    # if request.method =='POST':
                    #         u_form = UserUpdateForm(request.POST, instance=request.user)
                    #         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
                    #         # p_form = ProfileUpdateFormStudent(request.POST, request.FILES, instance=request.user.profile)
                    #
                    #
                    #         if u_form.is_valid() and p_form.is_valid():
                    #             u_form.save()
                    #             p_form.save()
                    #             messages.success(request, f'Your account has been updated!')
                    #             return redirect('profile')
                    #
                    #         else:
                    #             u_form = UserUpdateForm(instance=request.user)
                    #             p_form = ProfileUpdateForm(instance=request.user.profile)
                    #             # p_form = ProfileUpdateFormStudent(instance=request.user.profile)
                    #             # p_form.fields = ['image', 'bio', 'student', 'professional', 'test']
                    #         context = {
                    #             'u_form': u_form,
                    #             'p_form': p_form
                    #         }
                    #         return render(request, 'profile.html', context)
