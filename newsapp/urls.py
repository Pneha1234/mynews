from django.conf import settings
from django.conf.urls.static import static
from newsapp.views import *
import django.contrib
from django.urls import path


app_name = "newsapp"
urlpatterns = [


    # path('base/',ClientBaseView.as_view(),name='clientbase'),
    path('', ClientHomeView.as_view(), name='clienthome'),
    path('news/<int:pk>/detail/',
         ClientNewsDetailView.as_view(), name='clientnewsdetail'),

     path('', TemplateView.as_view(
        template_name='admintemplates/editorhome.html'), name='home'),
    path('subscriber/', SubscriberView.as_view(), name='subscriber'),

    path("subscriber/check/", SubscriberCheckView.as_view(), name="subscribercheck"),
    # editor url
    # editor url
    # editor url
    # editor url

    # editor NewsCategory
    # editor NewsCategory
    # editor NewsCategory
    # editor NewsCategory

    path('editor/', EditorNewsCategoryView.as_view(), name='editorhome'),
    path('editor/newscategory/',
         EditorNewsCategoryList.as_view(), name='newscategory'),
    path('editor/newscategoryadd',
         EditorNewsCategoryCreate.as_view(), name='newscategoryadd'),
    path('editor/<slug:slug>/newscategoryupdate/',
         EditorNewsCategoryUpdate.as_view(), name='newscategoryupdate'),
    path('editor/<slug:slug>/newscategorydelete/',
         EditorNewsCategoryDelete.as_view(), name='newscategorydelete'),
    path('editor/newslist/', EditorNewsList.as_view(), name='newslist'),

    # editor NewsSubCategory
    # editor NewsSubCategory
    # editor NewsSubCategory
    # editor NewsSubCategory

    path('editor/newssubcategorylist/',
         EditorNewsSubCategoryList.as_view(), name='newssubcategorylist'),
    path('editor/newssubcategoryadd',
         EditorNewsSubCategoryCreate.as_view(), name='newssubcategoryadd'),
    path('editor/<int:pk>/newssubcategoryupdate/',
         EditorNewsSubCategoryUpdate.as_view(), name='newssubcategoryupdate'),
    path('editor/<int:pk>/newssubcategorydelete/',
         EditorNewsSubCategoryDelete.as_view(), name='newssubcategorydelete'),
    # path('editor/<slug:slug>/newsdetail',
    #      EditorNewsDetailView.as_view(), name='newsdetail'),

    # editor news view
    # editor news view
    # editor news view
    # editor news view

    path('editor/newsadd/',
         EditorNewsCreate.as_view(), name='newsadd'),
    path('editor/<int:pk>/newsupdate/',
         EditorNewsUpdate.as_view(), name='newsupdate'),
    path('editor/<int:pk>/newsdelete/',
         EditorNewsDelete.as_view(), name='newsdelete'),

    path('editor-registration/',
         EditorRegistrationView.as_view(), name='editorregistration'),
    path('login/',
         LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),


    # admin url
    # admin url
    # admin url
    # admin url

    # admin advertizementposition view
    # admin advertizementposition view
    # admin advertizementposition view
    # admin advertizementposition view

    path('adminhome/', AdminView.as_view(), name='adminhome'),
    path('admin/adminadvetizementposition',
         AdminAdvertizementPositionList.as_view(), name='advertizementposition'),
    path('admin/advertizementpositionadd',
         AdminAdvertizementPositionCreate.as_view(), name='advertizementpositionadd'),
    path('admin/<int:pk>/advertizementpositionupdate',
         AdminAdvertizementPositionUpdate.as_view(), name='advertizementpositionupdate'),
    path('admin/<int:pk>/advertizementpositiondelete',
         AdminAdvertizementPositionDelete.as_view(), name='advertizementpositiondelete'),

    # admin advertizement view
    # admin advertizement view
    # admin advertizement view
    # admin advertizement view

    path('admin/adminadvettizement',
         AdminAdvertizementList.as_view(), name='advertizement'),
    path('admin/advertizementadd',
         AdminAdvertizementCreate.as_view(), name='advertizementadd'),
    path('admin/<int:pk>/advertizementupdate',
         AdminAdvertizementUpdate.as_view(), name='advertizementupdate'),
    path('admin/<int:pk>/advertizementdelete',
         AdminAdvertizementDelete.as_view(), name='advertizementdelete'),
    path('admin-registration/', AdminRegistrationView.as_view(),
         name='adminregistration'),


    # client url
    # client url
    # client url
    # client url
]
