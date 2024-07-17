from django import forms
from .models import * 

# class LeadWalaForm(forms.Form):
#         firstname = forms.CharField(max_length=200)
#         lastname = forms.CharField(max_length=200)
#         age = forms.IntegerField()
#         phoned = forms.BooleanField()
#         source = forms.ChoiceField(widget=forms.Select(), choices=Lead.data)
#         profilephoto = forms.ImageField()
#         special_files = forms.FileField()
#         agent = forms.ModelChoiceField(queryset=Agent.objects.all())
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
User = get_user_model()
class LeadWalaForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "firstname" ,
        "lastname" ,
        "age" ,
        "phoned" ,
        "source",
        "profilephoto" ,
        "special_files" ,
        "agent")

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

