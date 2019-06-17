from django import forms

from newsapp.models import *


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
