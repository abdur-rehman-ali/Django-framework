from django import forms

class studentRegistration(forms.Form):
    name = forms.CharField()
    reg = forms.IntegerField()