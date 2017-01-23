from django import forms

#testing form
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
