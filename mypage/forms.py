from django import forms
from first.models import User,Writer
from django.contrib.auth import password_validation,get_user_model

class UpdateuserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'email')
        widgets= {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'name' : forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': '아이디',
            'name': '이름',
            'email': '이메일',
        }


class ChangePasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': ('비밀번호가 일치하지 않습니다.'),
    }
    required_css_class = 'required'
    password1 = forms.CharField(
        label=("비밀번호"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'autofocus': True}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        # 조건
    )
    password2 = forms.CharField(
        label=("비밀번호 중복"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['비밀번호가 일치하지 않습니다.'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        """Save the new password."""
        password = self.cleaned_data["password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user

    @property
    def changed_data(self):
        data = super().changed_data
        for name in self.fields:
            if name not in data:
                return []
        return ['password']