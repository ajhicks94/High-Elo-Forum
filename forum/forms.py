from django import forms
from .models import Thread

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['forum', 'title', 'body']
        widgets = {
                'title': forms.TextInput(attrs={'value': 'Title'}), 
                'body': forms.Textarea(attrs={'value': 'Body'}),
        }
        #TODO: make forum field default to whichever forum the user clicked "Create New Thread" on

        
    #title = forms.CharField(label='Title', max_length=100,
                            #widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    #body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description'}),
                             #label='Body', max_length=40000)
    #forum = forms.CharField(widget=forms.TextInput(attrs={'value': 'thread.forum',
                                                          #'placeholder': 'Forum'}))