from django import forms
from django.forms import fields
from accounts.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'email', 'name','content']
