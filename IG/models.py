from django.db import models
from django.contrib.auth.models import User
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin

from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=44, null=True)
    bio = models.TextField()
    posts = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.bio




class Image(models.Model):
    image = models.ImageField(upload_to= 'images/', default="Image")
    image_name= models.CharField(max_length=44)
    image_caption= HTMLField()
    likes = models.IntegerField(default="0")
    comments = models.TextField(default="No Comment")
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_image_name(cls, searchname):
        image = cls.objects.filter(image_name__icontains=searchname)
        return image


    def __str__(self):
        return self.image_name


class Comments(models.Model):
    comment= models.CharField(max_length=255)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()


    def __str__(self):
        return self.comment
