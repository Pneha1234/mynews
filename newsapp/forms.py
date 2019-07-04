from django import forms
from newsapp.models import *
from .models import *


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsCategory
        fields = ['title', 'image', 'slug', 'icon_character']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter title...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'icon_character': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }

    # def __init__(self, *args, **kwargs):
    #     super(NewsForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'


class NewsSubCategoryForm(forms.ModelForm):

    class Meta:
        model = NewsSubCategory
        fields = ['title', 'main_category', 'image', 'icon_character']

    # def __init__(self, *args, **kwargs):
    #     super(NewsSubCategoryForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter title...'
            }),
            'main_category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(),

            'icon_character': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class EditorNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'main_category', 'sub_category',
                  'image', 'video_link', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter title...'
            }),
            'main_category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'sub_category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'video_link': forms.URLInput(attrs={
                'class': 'form-control',
            }),

            'content': forms.TextInput(attrs={
                'class': 'form-control',
            }),

        }

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

        widgets = {
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter position...'
            }),
        }


class AdminAdvertizement(forms.ModelForm):
    class Meta:
        model = Advertizement
        fields = ['organization', 'image', 'link']

    def __init__(self, *args, **kwargs):
        super(AdminAdvertizement, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AdminOrgnizationalInformation(forms.ModelForm):
    class Meta:
        model = OrgnizationalInformation
        fields = ['name', 'logo', 'address', 'slogan', 'contact_no',
                  'alt_contact_no', 'email', 'about_us', 'privacy_policy']


class EditorForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'enter  username....'
    }))
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'enter your full name ....'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'email....'
    }))
    contact_no = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'phone no...'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'enter you address..'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'enter password....'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'confirm password....'
    }))
    image = forms.FileInput(),
    about = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'write abour yourself.........'
    }))

    class Meta:
        model = Editor
        fields = [
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
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'enter  username....'
    }))
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'enter your full name ....'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'email....'
    }))
    contact_no = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'phone no...'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'enter you address..'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'enter password....'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'confirm password....'
    }))
    image = forms.FileField(widget=forms.ImageField),
    about = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'write abour yourself.........'
    }))

    class Meta:
        model = Admin
        fields = [
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


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'username..'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control input-lg',
        'placeholder': 'password'
    }))
    fields = ["username", "email", "password"]


##############
##########
######
####


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["commenter", "email", "comment"]
        widgets = {
            'commenter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'comment'}),

        }


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email"]
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Please enter your email...'
            })
        }
