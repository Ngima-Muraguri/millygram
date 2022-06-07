from django.test import TestCase
from .models import Image, Profile, Comments

from django.contrib.auth.models import User


# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.user = User(profile="Profile")
        self.user.save()

        self.new_image = Image(image="image", image_name="john", image_caption="Amazing", likes=1, comments="comment", profile=self.user)
        self.new_image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def tearDown(self):
        Image.objects.all().delete()

    def test_delete_image(self):
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertEqual(len(image), 0)

   


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(profile="Profile")
        self.user.save()

        self.new_profile = Profile(photo="image", name="john", bio="Amazing", posts=1, followers=1, following=1 ,user=self.user)
        self.new_profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def tearDown(self):
        Profile.objects.all().delete()

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertEqual(len(profile), 0)

        
class TestComments(TestCase):
    def setUp(self):
        self.user = User(profile="Profile")
        self.user.save()

        self.comment= Comments(comment="Comment", user=self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_comment(self):
        self.comment.save_comment()
        comment= Comments.objects.all()
        self.assertTrue(len(comment)>0)
