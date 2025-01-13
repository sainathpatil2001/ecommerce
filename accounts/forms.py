from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150, required=True)
    password = forms.CharField(label='Password', max_length=128, required=True, widget=forms.PasswordInput)
    verfy_password = forms.CharField(label='Verify Password', max_length=128, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email Address', required=True)

class EmailForm(forms.Form):
    email = forms.EmailField(label='Email Address', required=True)
