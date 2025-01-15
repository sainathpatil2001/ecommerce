from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150, required=True)
    password = forms.CharField(label='Password', max_length=128, required=True, widget=forms.PasswordInput)
    verfy_password = forms.CharField(label='Verify Password', max_length=128, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email Address', required=True)

class EmailForm(forms.Form):
    email = forms.EmailField(label='Email Address', required=True)


from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username',
        })
    )
    password = forms.CharField(
        label='Password',
        max_length=128,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
        })
    )
