from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import *


class ClientHomeView(ListView):
    template_name = 'clienttemplates/clienthome.html'
    model = NewsCategory
    context_object_name = 'clientcategorylist'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newslist'] = News.objects.all()
        context['maincategorylist'] = NewsCategory.objects.all()
        context['topviewednews'] = News.objects.order_by('view_count')
        context['popularnews'] = News.objects.order_by('-view_count')
        context['hotnews'] = News.objects.order_by('created_at')
        context['mostcommented'] = Comment.objects.order_by('-comment')
        context['newseditor'] = Editor.objects.all()
        context['advertiselist'] = Advertizement.objects.all()
        return context


class ClientNewsDetailView(DetailView):
	template_name = 'clienttemplates/newsdetail'
	model = News
	context_object_name = 'clientnewsdetail'

