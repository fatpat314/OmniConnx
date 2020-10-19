from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)

    student = models.BooleanField(null=True)
    professional = models.BooleanField(null=True)

    skills_to_offer = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True,null=True)
    looking_for = models.TextField(blank=True, null=True)

    affiliation = models.BooleanField(null=True)



    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        img = img.convert('RGB')

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
