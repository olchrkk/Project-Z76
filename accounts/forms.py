from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    bio = forms.CharField(required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'photo')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords didn't match!")
        return data['password2']

        # elif len(data['password2']) < 8:
        #     raise forms.ValidationError("Password must be more than 8 characters")
        # return data['password2']
