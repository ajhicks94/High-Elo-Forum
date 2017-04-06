from django import forms

class ThreadForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
