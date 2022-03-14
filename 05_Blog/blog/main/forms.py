from django import forms
from .models import Post

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","description","author")
        widgets ={
            'title': forms.TextInput(attrs={
                'class':'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class':'form-control',
            }),
            'author': forms.Select(attrs={
                'class':'form-control',
            }),
        }

class postUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","description")
        widgets ={
            'title': forms.TextInput(attrs={
                'class':'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class':'form-control',
            }),
        }
