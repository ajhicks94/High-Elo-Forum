from django import forms
from .models import Thread, Forum, Post
from django.contrib.auth.models import User

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['forum', 'title', 'body']
        widgets = {
                'title': forms.TextInput(attrs={'placeholder': 'Title'}), 
                'body': forms.Textarea(attrs={'placeholder': "Body"}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['thread', 'body']
        widgets = {
                'body': forms.Textarea(attrs={'placeholder': "Enter your response"}),
        }
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
                'username': forms.TextInput(attrs={'placeholder': 'choose a username'}),
                'password': forms.PasswordInput(attrs={'placeholder': 'enter password'}),
                #'verify_password': forms.TextInput(attrs={'placeholder': 'verify password'}),
                'email': forms.TextInput(attrs={'placeholder': 'email'}),
        }
