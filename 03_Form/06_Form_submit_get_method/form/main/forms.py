from django import forms

class registration(forms.Form):
    name = forms.CharField()
    reg = forms.IntegerField()
