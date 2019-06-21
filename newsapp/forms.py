from django import forms

from newsapp.models import *
from .models import *


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsCategory
        fields = ['title', 'image', 'slug', 'icon_character']

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsSubCategoryForm(forms.ModelForm):

    class Meta:
        model = NewsSubCategory
        fields = ['title', 'main_category', 'image', 'icon_character']

    def __init__(self, *args, **kwargs):
        super(NewsSubCategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EditorNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'main_category', 'sub_category',
                  'image', 'video_link', 'content', 'editor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_category'].queryset = NewsSubCategory.objects.none()

        if 'main_category' in self.data:
            
            category_id = int(self.data.get('main_category'))
            self.fields['sub_category'].queryset = NewsSubCategory.objects.filter(
                main_category_id=category_id).order_by('title')
            


class AdminAdvertizementPosition(forms.ModelForm):
    class Meta:
        model = AdvertizementPosition
        fields = ['position']

    def __init__(self, *args, **kwargs):
        super(AdminAdvertizementPosition, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AdminAdvertizement(forms.ModelForm):
    class Meta:
        model = Advertizement
        fields = ['organization', 'image', 'link', 'expiry_date']

    def __init__(self, *args, **kwargs):
        super(AdminAdvertizement, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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
