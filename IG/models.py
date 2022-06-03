from django.db import models
from django import forms
import datetime as dt
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('pictures')
    image_date = models.DateTimeField(auto_now_add=True ,null=True)
    name = models.CharField(max_length =30)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    # save image
    def save_image(self):
        self.save()

    # delete image
    def delete_image(self):
        self.delete()
    # get all images
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images
    # update image caption
    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
    # search images by name
    @classmethod
    def search_images(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term).all()
        return images


class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'pictures/')
    bio=models.TextField()
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    user_name=models.CharField(max_length=20,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()

    # update profile
    def update_profile(self, name):
        self.name = name
        self.save()

    # delete profile from database
    def delete_profile(self):
        self.delete()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    @classmethod
    def search_profiles(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term).all()
        return profiles