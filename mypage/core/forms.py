from django import forms
from .validators import validate_email
class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    terms_and_conditions = forms.BooleanField(required=True)