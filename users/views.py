from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateFormNone, ProfileUpdateFormStudent, ProfileUpdateFormProfessional, ProfileUpdateFormBoth
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from users.models import Friend_request, Profile, Messages
from django.db.models import Q



def view_messages(request):
    profile = Profile.objects.get(user=request.user)
    print('Profile: ', profile)
    message = Messages.objects.all()
    print("message: ", message.__dict__)
    qs = Messages.objects.messages_received(profile)
    print('QS: ', qs[0].text)
    results = list(map(lambda x: x.sender, qs))
    content = list(map(lambda x: x.text, qs))
    # for i in range(len(results)):
    #     content = list(map(lambda x: x.text, qs))[i]
    #     content2 = list(map(lambda x: x.text, qs))[0]
    # content = text
    print('result: ',results)
    is_empty = False
    if len(results) == 0:
        is_empty = True

    context = {
        'qs': results,
        'is_empty': is_empty,
        'content': content,
        'message': message
    }

    return render(request, 'messages.html', context)

def message_detail(request):
    profile = Profile.objects.get(user=request.user)
    qs = Messages.objects.messages_received(profile)
    content = list(map(lambda x: x.text, qs))[0]
    print('QS: ', qs)
    results = list(map(lambda x: x.sender, qs))
    print('result: ',results)
    is_empty = False
    if len(results) == 0:
        is_empty = True

    context = {
        'qs': results,
        'is_empty': is_empty,
        'content': content,
    }

    return render(request, 'message-detail.html', context)



def get_user_profile(request, username):
    # print("HEY!!!!!!")
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    print(profile)
    print(profile.user.username)
    rel_r = Friend_request.objects.filter(sender=profile)
    rel_s = Friend_request.objects.filter(receiver=profile)
    rel_receiver = []
    print("receiver: ",rel_receiver)
    rel_sender = []
    print("sender: ",rel_sender)
    for item in rel_r:
        rel_receiver.append(item.receiver.user)
    for item in rel_s:
        rel_sender.append(item.sender.user)

    context = {
        "rel_receiver": rel_receiver,
        "rel_sender": rel_sender,
    }

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

    profile = Profile.objects.get(user=request.user)
    # Get ID information of user
    thisUser = request.user.id
    # print("This user: ", thisUserName)
    same_user = ProfileUpdateFormNone.Meta.model.objects.values('user_id')
    all_users = ProfileUpdateFormNone.Meta.model.objects.values()


    for all in all_users:
        if all['student'] == True and all['professional'] == False:
            confirm = False
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
                            confirm = True
                            messages.success(request, f'Your account has been updated!')
                            return redirect('profile')
                    else:
                        u_form = UserUpdateForm(instance=request.user)
                        p_form = ProfileUpdateFormStudent(instance=request.user.profile)
                    context = {
                        'profile': profile,
                        'u_form': u_form,
                        'p_form': p_form,
                        'confirm': confirm
                    }
                    return render(request, 'profile.html', context)

        elif all['student'] == False and all['professional'] == True:
            confirm = False
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
                            confirm = True
                            messages.success(request, f'Your account has been updated!')
                            return redirect('profile')
                    else:
                        u_form = UserUpdateForm(instance=request.user)
                        p_form = ProfileUpdateFormProfessional(instance=request.user.profile)
                    context = {
                        'profile': profile,
                        'u_form': u_form,
                        'p_form': p_form,
                        'confirm': confirm
                    }
                    return render(request, 'profile.html', context)

        elif all['student'] == True and all['professional'] == True:
            confirm = False
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
                            confirm = True
                            messages.success(request, f'Your account has been updated!')
                            return redirect('profile')
                    else:
                        u_form = UserUpdateForm(instance=request.user)
                        p_form = ProfileUpdateFormBoth(instance=request.user.profile)
                    context = {
                        'profile': profile,
                        'u_form': u_form,
                        'p_form': p_form,
                        'confirm': confirm
                    }
                    return render(request, 'profile.html', context)

        else:
            confirm = False
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
                            confirm = True
                            messages.success(request, f'Your account has been updated!')
                            return redirect('profile')
                    else:
                        u_form = UserUpdateForm(instance=request.user)
                        p_form = ProfileUpdateFormNone(instance=request.user.profile)
                    context = {
                        'u_form': u_form,
                        'p_form': p_form,
                        'profile': profile,
                        'confirm': confirm
                    }
                    return render(request, 'profile.html', context)


@login_required
def send_invatation(request):
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Friend_request.objects.create(sender=sender, receiver=receiver, status='send')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile-edit')

@login_required
def remove_from_friends(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Friend_request.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile-edit')


@login_required
def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Friend_request.objects.invatations_received(profile)
    results = list(map(lambda x: x.sender, qs))
    is_empty = False
    if len(results) == 0:
        is_empty = True

    context = {
        'qs': results,
        'is_empty': is_empty,
    }

    return render(request, 'my_invites.html', context)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile-display.html'

    def get_object(self, slug=None):
        slug = self.kwargs.get('slug')
        print("slug: ", slug)
        profile = Profile.objects.get(slug=slug)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=str(self.request.user))
        profile = Profile.objects.get(user=user)
        rel_r = Friend_request.objects.filter(sender=profile)
        rel_s = Friend_request.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context['rel_receiver'] = rel_receiver
        context['rel_sender'] = rel_sender
        # context['posts'] = pk.get_object().get_all_suthors
        return context


class ProfileListView(ListView):
    model = Profile
    template_name = 'profile_list.html'
    context_object_name = 'qs'


    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Friend_request.objects.filter(sender=profile)
        rel_s = Friend_request.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context['rel_receiver'] = rel_receiver
        context['rel_sender'] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] = True
        return context


def invite_profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)
    # results = list(map(lambda x: x.sender, qs))
    # is_empty = False
    # if len(results) == 0:
    #     is_empty = True

    context = {
        'qs': qs#results,
        # 'is_empty': is_empty,
    }

    return render(request, 'to_invite_list.html', context)

@login_required
def accept_invatation(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Friend_request, sender=sender, receiver=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()
    return redirect('my-invites-view')

def reject_invatation(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        receiver = Profile.objects.get(user=request.user)
        sender = Profile.objects.get(pk=pk)
        rel = get_object_or_404(Friend_request, sender=sender, receiver=receiver)
        rel.delete()
    return redirect('my-invites-view')
