from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your username'}))

class RegistrationForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'firstname', 'placeholder': 'Type your firstname'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'lastname', 'placeholder': 'Type your lastname'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Type your email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password', 'placeholder': 'Type your password again'}))