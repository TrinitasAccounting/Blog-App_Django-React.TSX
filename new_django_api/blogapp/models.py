from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_img", blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.username


class Blog(models.Model):

    CATEGORY = (
        ("Technology", "Technology"),
        ("Economy", "Economy"),
        ("Business", "Business"),
        ("Sports", "Sports"),
        ("Lifestyle", "Lifestyle"),
    )


    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    # THe below foreign key, is actually connecting to our user that we have in settings.py file. It will be connected to that user, and if the user is deleted then we just set the user to null and keep the blog
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="blogs", null=True)  
    created_at = models.DateTimeField(auto_now_add=True)    #auto_now_add captures the time the blog was first created
    updated_at = models.DateTimeField(auto_now=True)   #auto_now captures the time the blog was updated
    published_time = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    category= models.CharField(max_length=255, choices=CATEGORY, blank=True, null=True)
    featured_image = models.ImageField(upload_to="blog_img", blank=True, null=True)


    # This is saying how to order the blogs (not sure if we need this or not, we may can handle this easier in react)
    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title
