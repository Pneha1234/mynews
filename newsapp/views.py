from django.shortcuts import render
from django.views.generic import *

# Create your views here.
class ClientBaseView(TemplateView):
	template_name = 'clienttemplates/clientbase.html'