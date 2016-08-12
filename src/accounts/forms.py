from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    last_name=forms.CharField(max_length=10)
    first_name=forms.CharField(max_length=10)
    email=forms.EmailField()

    def save(self, commit=True):
        user=super(SignupForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.last_name=self.cleaned_data['last_name']
        user.first_name=self.cleaned_data['first_name']

        if commit:
            user.save()
        return user

    class Meta:
        model=User
        fields=('username', 'password1', 'password2', 'email', 'last_name', 'first_name')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디를 입력하세요.'
        self.fields['password1'].label = '비밀번호를 입력하세요.'
        self.fields['password2'].label = '비밀번호를 다시 한 번 입력하세요.'
        self.fields['email'].label = '이메일을 입력하세요.'
        self.fields['last_name'].label = '성을 적어주세요.'
        self.fields['first_name'].label = '이름을 적어주세요.'

    def clean_email(self):
        data=self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('이미 동일한 이메일이 존재합니다.')
        return data


