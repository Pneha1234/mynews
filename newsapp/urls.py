from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
from newsapp.views import *
import django.contrib
from django.urls import path
from django.views.generic.base import TemplateView

app_name = "newsapp"
urlpatterns = [

	path('', TemplateView.as_view(template_name='admintemplates/editorhome.html'), name='home'), # new
	path('base/',ClientBaseView.as_view(),name='clientbase')


]