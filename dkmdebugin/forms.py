from django import forms

class ContactForm(forms.Form):
    name        = forms.CharField(max_length=50)
    email       = forms.EmailField()
    message     = forms.CharField(widget=forms.Textarea)
