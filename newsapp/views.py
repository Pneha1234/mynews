from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *

from django.views.generic.edit import *

from .models import *
from django.shortcuts import get_object_or_404


# class NewsCategoryList(ListView):
#     template_name = 'admintemplates/editorhome.html'
#     model = NewsCategory
#     context_object_name = 'newscategory'

#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)
#         context['newslist'] = News.objects.all()
#         return context

# Create your views here.
class ClientBaseView(TemplateView):
    template_name = 'clienttemplates/clientbase.html'
