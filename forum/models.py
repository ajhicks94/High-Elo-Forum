from django.db import models
from django.utils import timezone
from django.db.models import F
from django.conf import settings

class Profile(models.Model):

    user       = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group      = models.CharField(max_length=15, default='Normie') #pretty sure this is done in AUTH USER
    post_count = models.IntegerField(default=0)
    rep_count  = models.IntegerField(default=0)
    #email addr
    #ip addr
    server     = models.CharField(max_length=26, default='Unknown')
    rank       = models.CharField(max_length=16, default='Paper V')

    def __str__(self):
        return self.user.username

    def increase_post_count(self):
        Profile.objects.filter(pk=self.pk).update(post_count=F('post_count') + 1)

class Category(models.Model): #ie. Junkies, Non-Junkies

    name     = models.CharField(max_length=70)
    position = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Forum(models.Model): #ie. Ask a Gladiator -> General Questions, LoL -> Guides

    name         = models.CharField(max_length=50)
    category     = models.ForeignKey(Category, on_delete=models.PROTECT)
    position     = models.IntegerField(default=0)
    #description field?
    post_count   = models.IntegerField(default=0)
    thread_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Thread(models.Model): #ie. FULL GUIDE TO HOW TO BEAT DARIUS THE COCKMUNCHER
    
    forum      = models.ForeignKey(Forum, on_delete=models.CASCADE)
    author     = models.ForeignKey(settings.AUTH_USER_MODEL)
    title      = models.CharField(max_length=200)
    created    = models.DateTimeField(auto_now_add=True)
    modified   = models.DateTimeField(auto_now=True)
    post_count = models.IntegerField(default=0)
    sticky     = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Post(models.Model): #Wow I never thought about it this way man, great job!

    thread   = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    body     = models.TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
