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