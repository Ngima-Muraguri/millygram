from django import forms
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Image, Profile, Comments

class AddImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption','name']
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']
class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['content']
        widgets= {
            'content':forms.Textarea(attrs={'rows':2,})
        }