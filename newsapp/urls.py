from django.conf import settings
from django.conf.urls.static import static
from newsapp.views import *
import django.contrib
from django.urls import path


app_name = "newsapp"
urlpatterns = [

    # editor url
    # editor url
    # editor url
    # editor url

    path('editor/', EditorNewsCategoryView.as_view(), name='home'),
    path('editor/newscategory', EditorNewsCategoryList.as_view(), name='newscategory'),
    path('editor/newscategoryadd',
         EditorNewsCategoryCreate.as_view(), name='newscategoryadd'),
    path('editor/<slug:slug>/newscategoryupdate',
         EditorNewsCategoryUpdate.as_view(), name='newscategoryupdate'),
    path('editor/<slug:slug>/newscategorydelete',
         EditorNewsCategoryDelete.as_view(), name='newscategorydelete'),
    path('editor/<slug:slug>/newsdetail',
         EditorNewsDetailView.as_view(), name='newsdetail'),
    path('editor/newsadd',
         EditorNewsCreate.as_view(), name='newsadd'),
    path('editor/<slug:slug>/newsupdate',
         EditorNewsUpdate.as_view(), name='newsupdate'),
    path('editor/<slug:slug>/newsdelete',
         EditorNewsDelete.as_view(), name='newsdelete'),

    # admin url
    # admin url
    # admin url
    # admin url

    path('adminhome/', AdminView.as_view(), name='adminhome'),
    path('admin/adminadvettizement',
         AdminAdvertizementPositionList.as_view(), name='advertizementposition'),
    path('admin/advertizementpositionadd',
         AdminAdvertizementPositionCreate.as_view(), name='advertizementpositionadd'),
    path('admin/<int:pk>/advertizementpositionupdate',
         AdminAdvertizementPositionUpdate.as_view(), name='advertizementpositionupdate'),
    path('admin/<int:pk>/advertizementpositiondelete',
         AdminAdvertizementPositionDelete.as_view(), name='advertizementpositiondelete'),

    #client url
    path('',ClientHomeView.as_view(),name='clienthome'),




	path('', TemplateView.as_view(template_name='admintemplates/editorhome.html'), name='home'), 




]


	



