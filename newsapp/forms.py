from django import forms

from newsapp.models import *
from .models import *


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsCategory
        fields = ['title', 'image', 'slug', 'icon_character']


class EditorNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'slug', 'image', 'video_link', 'content']


class AdminAdvertizementPosition(forms.ModelForm):
    class Meta:
        model = AdvertizementPosition
        fields = ['position']


class AdminAdvertizement(forms.ModelForm):
    class Meta:
        model = Advertizement
        fields = ['organization', 'image', 'link', 'expiry_date']


class EditorForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Editor
        fields = ["username", "password", "confirm_password",
                  "full_name", "contact_no", "address", "email", "image", "about"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError(
                "user with this username already exist")

        return username

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        c_password = self.cleaned_data.get("confirm_password")
        if password != c_password:
            raise forms.ValidationError("password didn't match")

        return c_password


class AdminForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Admin
        fields = ["username", "password", "confirm_password",
                  "full_name", "contact_no", "address", "email", "image", "about"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError(
                "user with this username already exists"
            )
        return username

    def clen_confirm_password(self):
        password = self.cleaned_data.get("password")
        c_password = self.cleaned_data.get("confirm_password")
        if password != c_password:
            raise forms.ValidationError(
                "password didn't match"
            )

        return c_password


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
