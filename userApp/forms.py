from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username', 'first_name', 'last_name', 'email', 'affiliation', 'nationality',
            'password1', 'password2'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "email universitaire"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if hasattr(user, 'role'):
            user.role = 'participant'
        if commit:
            user.save()
        return user
