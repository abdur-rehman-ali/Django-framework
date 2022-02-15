from django import  forms

class InputForm(forms.Form):
    name = forms.CharField()
    reg = forms.IntegerField(
        help_text='Enter 6 digit roll number'
    )
    password = forms.CharField(widget=forms.PasswordInput())
    key = forms.CharField(widget=forms.HiddenInput())