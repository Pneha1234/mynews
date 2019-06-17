from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.views.generic.edit import *
from newsapp.forms import *
from .models import *

# Editor Views
# Editor Views
# Editor Views
# Editor Views


class EditorNewsCategoryView(TemplateView):
    template_name = 'admintemplates/editorhome.html'


class EditorNewsCategoryCreate(CreateView):
    template_name = "admintemplates/editornewscategoryadd.html"
    model = NewsCategory
    form_class = NewsForm
    success_url = reverse_lazy('newsapp:newscategory')


class EditorNewsCategoryList(ListView):
    template_name = 'admintemplates/editornewscategorylist.html'
    model = NewsCategory
    context_object_name = 'newscategorylist'


class EditorNewsCategoryUpdate(UpdateView):
    template_name = 'admintemplates/editornewscategoryupdate.html'
    model = NewsCategory
    fields = ['title', 'image', 'icon_character']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:newscategory')


class EditorNewsCategoryDelete(DeleteView):
    template_name = "admintemplates/editornewscategorydelete.html"
    model = NewsCategory
    success_url = reverse_lazy('newsapp:newscategory')


class EditorNewsDetailView(DetailView):
    template_name = "admintemplates/editornewsdetail.html"
    model = NewsCategory
    context_object_name = 'newsdetail'


class EditorNewsCreate(CreateView):
    template_name = 'admintemplates/editornewsadd.html'
    model = News
    form_class = EditorNewsForm
    context_object_name = 'newscreate'
    success_url = reverse_lazy('newsapp:newsdetail')


class EditorNewsUpdate(UpdateView):
    template_name = 'admintemplates/editornewsupdate.html'
    model = News
    fields = ['title', 'slug', 'image', 'video_link', 'content']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:newsdetail')


class EditorNewsDelete(DeleteView):
    template_name = 'admintemplates/editornewsdelete.html'
    model = News
    success_url = reverse_lazy('newsapp:newsdetail')


# Admin Views
# Admin Views
# Admin Views
# Admin Views

class AdminView(TemplateView):
    template_name = 'admintemplates/adminhome.html'


class AdminAdvertizementPositionList(ListView):
    template_name = 'admintemplates/adminadvertizementlist.html'
    model = AdvertizementPosition
    context_object_name = 'advertizementpositionlist'


class AdminAdvertizementPositionCreate(CreateView):
    template_name = "admintemplates/adminadvertizementadd.html"
    model = AdvertizementPosition
    form_class = AdminAdvertizementPosition
    success_url = reverse_lazy('newsapp:advertizementposition')


class AdminAdvertizementPositionUpdate(UpdateView):
    template_name = 'admintemplates/adminadvertizementupdate.html'
    model = AdvertizementPosition
    fields = ['position']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:advertizementposition')


class AdminAdvertizementPositionDelete(DeleteView):
    template_name = 'admintemplates/adminadvertizementdelete.html'
    model = AdvertizementPosition
    success_url = reverse_lazy('newsapp:advertizementposition')
