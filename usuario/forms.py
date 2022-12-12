from django.forms import ModelForm
from .models import Project
from taggit.forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title','description','photo','url','tags')
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'photo': 'Imágen',
            'url': 'URL de Github',
            'tags': 'Tags'

        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name","email","password1","password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user