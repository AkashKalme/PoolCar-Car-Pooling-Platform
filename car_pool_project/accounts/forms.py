from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = 'form-control'
        self.fields["email"].widget.attrs["class"] = 'form-control'
        self.fields["password1"].widget.attrs["class"] = 'form-control'
        self.fields["password2"].widget.attrs["class"] = 'form-control'
        self.fields["username"].widget.attrs["class"] = 'form-control-lg'
        self.fields["password1"].widget.attrs["class"] = 'form-control-lg'
        self.fields["email"].widget.attrs["class"] = 'form-control-lg'
        self.fields["password2"].widget.attrs["class"] = 'form-control-lg'
        self.fields["username"].widget.attrs["id"] = 'username'
        self.fields["email"].widget.attrs["id"] = 'email'
        self.fields["password1"].widget.attrs["id"] = 'password1'
        self.fields["password2"].widget.attrs["id"] = 'password2'
        self.fields["username"].label = ""
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields["username"].widget.attrs["placeholder"] = 'User Name'
        self.fields["email"].widget.attrs["placeholder"] = 'Email Address'
        self.fields["password1"].widget.attrs["placeholder"] = 'Password'
        self.fields["password2"].widget.attrs["placeholder"] = 'Re-enter Password'
        self.fields["username"].help_text = None
        self.fields["email"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
