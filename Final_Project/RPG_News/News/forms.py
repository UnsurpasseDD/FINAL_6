from datetime import date
from django import forms
#from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
 





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        