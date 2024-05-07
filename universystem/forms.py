from django import forms
from django.contrib.auth.models import User
from .models import Profile, Lectures, Lectures_text, Application


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data        
        if cd['password'] != cd['password2']:            
            raise forms.ValidationError('Passwords don\'t match.')        
        return cd['password2']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['photo']

class LecturesForm(forms.ModelForm):

    class Meta:
        model = Lectures
        fields = ['name', 'value']

class LecturesTextForm(forms.ModelForm):

    class Meta:
        model = Lectures_text
        fields = ['lectures_id', 'title', 'text', 'photo']


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['name', 'text']