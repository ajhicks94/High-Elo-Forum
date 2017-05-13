from django import forms
from .models import Thread, Forum

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['forum', 'title', 'body']
        widgets = {
                'title': forms.TextInput(attrs={'value': 'Title'}), 
                'body': forms.Textarea(attrs={'value': 'Body'}),
        }
        #TODO: make forum field default to whichever forum the user clicked "Create New Thread" on
