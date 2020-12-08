from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models import Q
from django.template.defaultfilters import slugify
from .utils import get_random_code
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.shortcuts import reverse




class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Friend_request.objects.filter(Q(sender=profile) | Q(receiver=profile))
        print(qs)
        print("-----------------")

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print("-----------------")
        return available




    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, default=None)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)

    student = models.BooleanField(null=True)
    professional = models.BooleanField(null=True)

    skills_to_offer = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True,null=True)
    looking_for = models.TextField(blank=True, null=True)

    affiliation = models.BooleanField(null=True)

    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    objects = ProfileManager()


    def get_friends(self):
        return self.friends.all()

    def get_friends_number(self):
        return self.friends.all().count()

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse("profile-detail-view", kwargs={"slug": self.slug}),

    def save(self, *args, **kwargs):

        super().save()

        img = Image.open(self.image.path)
        img = img.convert('RGB')

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Profile)

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted'),
)

class Friend_request_manager(models.Manager):
    def invatations_received(self, receiver):
        qs = Friend_request.objects.filter(receiver=receiver, status='send')
        return qs

    # Friend_request.objects.invatations_received(profile)

class Friend_request(models.Model):
    sender = models.ForeignKey(Profile, related_name='sender', on_delete=models.CASCADE, default=None)
    receiver = models.ForeignKey(Profile, related_name='receiver', on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=None)
    # timestamp = DateTimeField(auto_now_add=True)

    objects = Friend_request_manager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

class Messages_manager(models.Manager):
    def messages_received(self, receiver):
        qs = Messages.objects.filter(receiver=receiver, status='send')
        return qs


class Messages(models.Model):
    sender = models.ForeignKey(Profile, related_name='message_sender', on_delete=models.CASCADE, default=None)
    receiver = models.ForeignKey(Profile, related_name='message_receiver', on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=None)
    text = models.TextField()

    objects = Messages_manager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}-{self.text}"
