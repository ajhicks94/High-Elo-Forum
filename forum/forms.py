from django import forms

#testing form
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ThreadForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
