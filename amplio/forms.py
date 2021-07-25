from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Select, Textarea
from captcha.fields import CaptchaField
from .models import registration

grades =(
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)

webinarDates =(
    ("July 24", "July 24"),
)

class WebinarForm(ModelForm):
    class Meta:
        model = registration
        fields = ['name', 'grade', 'email', 'date', 'extraInfo']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
            }),
            'grade': Select(choices=grades),
            'email': EmailInput(attrs={
                'class': "form-control",
            }),
            'date': Select(choices=webinarDates),
            'extraInfo': Textarea(attrs={
                'class': "form-control",
            }),
        }
    captcha = CaptchaField()
