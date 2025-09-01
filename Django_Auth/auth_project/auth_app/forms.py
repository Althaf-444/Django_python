from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput , label="confirm password")

    class Meta:
        model = User
        fields = ['username','password']

    def clean(self):
        cleaned_data = super().clean()  
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('password_confirm')

        if password and confirmPassword and password != confirmPassword:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data