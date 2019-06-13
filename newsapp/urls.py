from django.conf import settings
from django.conf.urls.static import static
from newsapp.views import *
import django.contrib
from django.urls import path
from django.views.generic.base import TemplateView

app_name = "newsapp"
urlpatterns = [

	#path('base/',ClientBaseView.as_view(),name='clientbase'),
	path('',ClientHomeView.as_view(),name='clienthome'),




	path('', TemplateView.as_view(template_name='admintemplates/editorhome.html'), name='home'), 

]