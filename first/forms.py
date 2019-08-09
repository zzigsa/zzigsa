from django import forms
from .models import User

#로그인
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': '아이디',
            'password': '비밀번호',
        }
        