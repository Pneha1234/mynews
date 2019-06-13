from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
#class ClientBaseView(TemplateView):
	#template_name = 'clienttemplates/clientbase.html'


class ClientHomeView(ListView):
	template_name = 'clienttemplates/clienthome.html'
	model = NewsCategory
	context_object_name = 'clientcategorylist'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['newslist'] = News.objects.all()
		return context

#class ClientCategoryDetailView(ListView):
#	template_name = 'clienttemplates/categorydetail.html'
#	model = NewsSubCategory
#	context_object_name = 'clientcategorydetail'