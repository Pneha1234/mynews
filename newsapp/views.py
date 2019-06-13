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
        return context
