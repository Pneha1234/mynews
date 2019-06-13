from django.urls import path
from .views import *


app_name = "newsapp"
urlpatterns = [
	#path('base/',ClientBaseView.as_view(),name='clientbase'),
	path('',ClientHomeView.as_view(),name='clienthome'),
]