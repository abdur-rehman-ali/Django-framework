from django import forms


class formFields(forms.Form):
    CHOICES = (
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
        ("4", "Four"),
        ("5", "Five"),
    )

    name = forms.CharField(label='Enter your name', label_suffix="",
                           required=False, help_text="Enter you name", disabled=True, error_messages={'required': 'Enter you name'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'class1 class2',
        'id':'id1'
    }))
    rating = forms.ChoiceField(choices=CHOICES)