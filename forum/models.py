from django.db import models
from django.utils import timezone
from django.db.models import F
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def get_sentinel_user():
    return User.objects.get_or_create(username='[deleted]')[0]

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

class Category(models.Model):

    name     = models.CharField(max_length=70)
    position = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Forum(models.Model):

    name         = models.CharField(max_length=50)
    slug         = models.SlugField(max_length=55, editable=False)
    category     = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="forums")
    position     = models.IntegerField(default=0)
    description  = models.CharField(max_length=255, default='Description goes here')
    post_count   = models.IntegerField(default=0, editable=False)
    thread_count = models.IntegerField(default=0, editable=False)

    #def get_post_count(self):
        #post_count = SUM OF POST COUNT OF ALL THREADS

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
            super(Forum, self).save(*args, **kwargs)
        else:
            super(Forum, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Thread(models.Model): #ie. FULL GUIDE TO HOW TO BEAT DARIUS THE COCKMUNCHER
    
    forum      = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="threads")
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    title      = models.CharField(max_length=90)
    body       = models.TextField()
    slug       = models.SlugField(max_length=95, editable=True)
    created    = models.DateTimeField(auto_now_add=True)
    modified   = models.DateTimeField(auto_now=True)
    post_count = models.IntegerField(default=0)
    sticky     = models.BooleanField(default=False)

    def increase_thread_count(self):
        Forum.objects.filter(pk=self.forum.pk).update(thread_count=F('thread_count') + 1)

    def decrease_thread_count(self):
        Forum.objects.filter(pk=self.forum.pk).update(thread_count=F('thread_count') - 1)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.increase_thread_count()
            self.slug = slugify(self.title)
            super(Thread, self).save(*args, **kwargs)
        else:
            super(Thread, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):

    thread   = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    body     = models.TextField()

    def increase_post_count(self):
        Thread.objects.filter(pk=self.thread.pk).update(post_count=F('post_count') + 1)

    def decrease_post_count(self):
        Thread.objects.filter(pk=self.thread.pk).update(post_count=F('post_count') - 1)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.increase_post_count()
            super(Post, self).save(*args, **kwargs)
        else:
            super(Post, self).save(*args, **kwargs)
            
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
@receiver(post_delete, sender=Post)
def delete_post(sender, instance, **kwargs):
    instance.decrease_post_count()

@receiver(post_delete, sender=Thread)
def delete_thread(sender, instance, **kwargs):
    instance.decrease_thread_count()
