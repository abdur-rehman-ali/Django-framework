from django import forms

class registration(forms.Form):
    name = forms.CharField(max_length=3)
    reg = forms.IntegerField(max_value=20)
