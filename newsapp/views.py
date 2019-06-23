from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.views.generic.edit import *
from newsapp.forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib. auth import authenticate, login, logout
from .forms import *


# Editor Views
# Editor Views
# Editor Views
# Editor Views


class EditorRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.groups.filter(name="Editor").exists():
            pass
        else:
            return redirect("/login/")
        return super().dispatch(request, *args, **kwargs)

# NewsCategory View
# NewsCategory View
# NewsCategory View
# NewsCategory View


class EditorNewsCategoryView(EditorRequiredMixin, TemplateView):
    template_name = 'admintemplates/editorhome.html'


class EditorNewsCategoryCreate(EditorRequiredMixin, CreateView):
    template_name = "admintemplates/editornewscategoryadd.html"
    model = NewsCategory
    form_class = NewsForm
    success_url = reverse_lazy('newsapp:newscategory')


class EditorNewsCategoryList(EditorRequiredMixin, ListView):
    template_name = 'admintemplates/editornewscategorylist.html'
    model = NewsCategory
    context_object_name = 'newscategorylist'


class EditorNewsCategoryUpdate(EditorRequiredMixin, UpdateView):
    template_name = 'admintemplates/editornewscategoryupdate.html'
    model = NewsCategory

    fields = ['title', 'image', 'icon_character']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:newscategory')


class EditorNewsCategoryDelete(EditorRequiredMixin, DeleteView):
    template_name = "admintemplates/editornewscategorylist.html"

    model = NewsCategory
    success_url = reverse_lazy('newsapp:newscategory')

# News SubCategory Views
# News SUbCategory Views
# News SubCategory Views
# News SubCategory Views


class EditorNewsSubCategoryList(EditorRequiredMixin, ListView):
    template_name = 'admintemplates/editornewssubcategorylist.html'
    model = NewsSubCategory
    context_object_name = 'newssubcategorylist'


class EditorNewsSubCategoryCreate(EditorRequiredMixin, CreateView):
    template_name = "admintemplates/editornewssubcategoryadd.html"
    model = NewsSubCategory
    form_class = NewsSubCategoryForm
    success_url = reverse_lazy('newsapp:newssubcategorylist')


class EditorNewsSubCategoryUpdate(EditorRequiredMixin, UpdateView):
    template_name = 'admintemplates/editornewssubcategoryupdate.html'
    model = NewsSubCategory
    fields = ['title', 'main_category', 'image', 'icon_character']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:newssubcategorylist')


class EditorNewsSubCategoryDelete(EditorRequiredMixin, DeleteView):
    template_name = "admintemplates/editornewssubcategorylist.html"
    model = NewsSubCategory
    success_url = reverse_lazy('newsapp:newssubcategorylist')


# News Views
# News Views
# News Views
# News Views

class EditorNewsList(EditorRequiredMixin, ListView):
    template_name = 'admintemplates/editornewslist.html'
    model = News
    context_object_name = 'newslist'


class EditorNewsDetailView(DetailView):
    template_name = "admintemplates/editornewsdetail.html"
    model = News
    context_object_name = 'newsdetail'


class EditorNewsCreate(EditorRequiredMixin, CreateView):
    template_name = 'admintemplates/editornewsadd.html'
    model = News
    form_class = EditorNewsForm
    context_object_name = 'newscreate'
    success_url = reverse_lazy('newsapp:newslist')


def load_subcategories(request):
    category_id = request.GET.get('main_category')
    print(category_id)
    sub_category = NewsSubCategory.objects.filter(
        main_category_id=category_id).order_by('title')
    print(sub_category)
    return render(request, 'admintemplates/subcategory_dropdown_list_options.html', {'sub_category': sub_category})


class EditorNewsUpdate(EditorRequiredMixin, UpdateView):
    template_name = 'admintemplates/editornewsupdate.html'
    model = News
    fields = ['title', 'main_category', 'sub_category',
              'image', 'video_link', 'content']
    tform_class = EditorNewsForm
    success_url = reverse_lazy('newsapp:newslist')


class EditorNewsDelete(EditorRequiredMixin, DeleteView):
    template_name = 'admintemplatesajax/load-subcategories//editornewsdetail.html'
    model = News
    success_url = reverse_lazy('newsapp:newslist')


class EditorRegistrationView(CreateView):
    template_name = "admintemplates/editorregistration.html"
    form_class = EditorForm
    success_url = reverse_lazy('newsapp:login')

    def form_valid(self, form):
        u_name = form.cleaned_data["username"]
        p_word = form.cleaned_data["password"]
        user = User.objects.create_user(u_name, "", p_word)
        form.instance.user = user
        return super().form_valid(form)


class AdminRegistrationView(CreateView):
    template_name = "admintemplates/adminregistration.html"
    form_class = AdminForm
    success_url = reverse_lazy('newsapp:login')

    def form_valid(self, form):
        u_name = form.cleaned_data["username"]
        p_word = form.cleaned_data["password"]
        user = User.objects.create_user(u_name, "", p_word)
        form.instance.user = user
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "admintemplates/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('newsapp:editor')

    def form_valid(self, form):
        u_name = form.cleaned_data["username"]
        p_word = form.cleaned_data["password"]

        user = authenticate(username=u_name, password=p_word)
        self.thisuser = user

        if user is not None and user.groups.exists():
            login(self.request, user)

        else:
            return render(self.request, self.template_name,
                          {"error": "username or password didn't match", "form": form})

        return super().form_valid(form)

    def get_success_url(self):
        if self.thisuser.groups.filter(name="Editor").exists():
            return reverse("newsapp:editorhome")
        elif self.thisuser.groups.filter(name="Admin").exists():
            return reverse("newsapp:adminhome")

        else:
            return reverse("newsapp:login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login/")


# Admin Views
# Admin Views
# Admin View
# Admin Views

class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.groups.filter(name="Admin").exists():
            pass
        else:
            return redirect("/login/")
        return super().dispatch(request, *args, **kwargs)

# admin advertizementposition view
# admin advertizementposition view
# admin advertizementposition view
# admin advertizementposition view


class AdminView(AdminRequiredMixin, TemplateView):
    template_name = 'admintemplates/adminhome.html'


class AdminAdvertizementPositionList(AdminRequiredMixin, ListView):
    template_name = 'admintemplates/adminadvertizementpositionlist.html'

    model = AdvertizementPosition
    context_object_name = 'advertizementpositionlist'


class AdminAdvertizementPositionCreate(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminadvertizementpositionadd.html"

    model = AdvertizementPosition
    form_class = AdminAdvertizementPosition
    success_url = reverse_lazy('newsapp:advertizementposition')


class AdminAdvertizementPositionUpdate(AdminRequiredMixin, UpdateView):
    template_name = 'admintemplates/adminadvertizementpositionupdate.html'

    model = AdvertizementPosition
    fields = ['position']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:advertizementposition')


class AdminAdvertizementPositionDelete(AdminRequiredMixin, DeleteView):
    template_name = 'admintemplates/adminadvertizementpositionlist.html'

    model = AdvertizementPosition
    success_url = reverse_lazy('newsapp:advertizementposition')

# admin advertizement view
# admin advertizement view
# admin advertizement view
# admin advertizement view


class AdminAdvertizementList(ListView):
    template_name = 'admintemplates/adminadvertizementlist.html'
    model = Advertizement
    context_object_name = 'advertizementlist'


class AdminAdvertizementCreate(CreateView):
    template_name = "admintemplates/adminadvertizementadd.html"
    model = Advertizement
    form_class = AdminAdvertizement
    success_url = reverse_lazy('newsapp:advertizementadd')


class AdminAdvertizementUpdate(UpdateView):
    template_name = 'admintemplates/adminadvertizementupdate.html'
    model = Advertizement
    fields = ['organization', 'image', 'link', 'expiry_date']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:advertizement')


class AdminAdvertizementDelete(DeleteView):
    template_name = 'admintemplates/adminadvertizementlist.html'
    model = Advertizement
    success_url = reverse_lazy('newsapp:advertizement')

# admin organization views
# admin organization views
# admin organization views
# admin organization views


class AdminOrganizationInformationList(ListView):
    template_name = 'admintemplates/adminorganizationinformationlist.html'
    model = OrgnizationalInformation
    context_object_name = 'organizationinformationlist'


class AdminOrganizationInformationDetail(DetailView):
    template_name = 'admintemplates/adminorganizationinformationdetail.html'
    model = OrgnizationalInformation
    context_object_name = 'organizationinformationdetail'


class AdminOrganizationInformationUpdate(UpdateView):
    template_name = 'admintemplates/adminorganizationinformationupdate.html'
    model = OrgnizationalInformation
    fields = ['name', 'logo', 'address', 'slogan', 'contact_no',
              'alt_contact_no', 'email', 'about_us', 'privacy_policy']

    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:organizationinformationlist')

# admin newscategory views
# admin newscategory views
# admin newscategory views
# admin newscategory views


class AdminNewsCategoryCreate(CreateView):
    template_name = "admintemplates/adminnewscategoryadd.html"
    model = NewsCategory
    form_class = NewsForm
    success_url = reverse_lazy('newsapp:adminnewscategorylist')


class AdminNewsCategoryList(ListView):
    template_name = 'admintemplates/adminnewscategorylist.html'
    model = NewsCategory
    context_object_name = 'adminnewscategorylist'


class AdminNewsCategoryUpdate(UpdateView):
    template_name = 'admintemplates/adminnewscategoryupdate.html'
    model = NewsCategory

    fields = ['title', 'image', 'icon_character']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:adminnewscategorylist')


class AdminNewsCategoryDelete(EditorRequiredMixin, DeleteView):
    template_name = "admintemplates/adminnewscategorylist.html"

    model = NewsCategory
    success_url = reverse_lazy('newsapp:adminnewscategorylist')

# admin newssubcategory views
# admin newssubcategory views
# admin newssubcategory views
# admin newssubcategory views


class AdminNewsSubCategoryList(ListView):
    template_name = 'admintemplates/adminnewssubcategorylist.html'
    model = NewsSubCategory
    context_object_name = 'adminnewssubcategorylist'


class AdminNewsSubCategoryCreate(CreateView):
    template_name = "admintemplates/adminnewssubcategoryadd.html"
    model = NewsSubCategory
    form_class = NewsSubCategoryForm
    success_url = reverse_lazy('newsapp:adminnewssubcategorylist')


class AdminNewsSubCategoryUpdate(UpdateView):
    template_name = 'admintemplates/adminnewssubcategoryupdate.html'
    model = NewsSubCategory
    fields = ['title', 'main_category', 'image', 'icon_character']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:adminnewssubcategorylist')


class AdminNewsSubCategoryDelete(DeleteView):
    template_name = "admintemplates/adminnewssubcategorylist.html"
    model = NewsSubCategory
    success_url = reverse_lazy('newsapp:adminnewssubcategorylist')

# admin news views
# admin news views
# admin news views
# admin news views


class AdminNewsList(ListView):
    template_name = 'admintemplates/adminnewslist.html'
    model = News
    context_object_name = 'adminnewslist'


class AdminNewsDetailView(DetailView):
    template_name = "admintemplates/adminnewsdetail.html"
    model = News
    context_object_name = 'adminnewsdetail'


class AdminNewsCreate(CreateView):
    template_name = 'admintemplates/adminnewsadd.html'
    model = News
    form_class = EditorNewsForm
    context_object_name = 'newscreate'
    success_url = reverse_lazy('newsapp:adminnewslist')


class AdminNewsUpdate(EditorRequiredMixin, UpdateView):
    template_name = 'admintemplates/adminnewsupdate.html'
    model = News
    fields = ['title', 'main_category', 'sub_category',
              'image', 'video_link', 'content']
    tform_class = EditorNewsForm
    success_url = reverse_lazy('newsapp:adminnewslist')


class AdminNewsDelete(EditorRequiredMixin, DeleteView):
    template_name = 'admintemplates/adminnewslist.html'
    model = News
    success_url = reverse_lazy('newsapp:adminnewslist')


# admin editor View
# admin editor View
# admin editor View
# admin editor View

class EditorList(ListView):
    template_name = 'admintemplates/admineditorlist.html'
    model = Editor
    context_object_name = 'admineditorlist'


class EditorCreate(CreateView):
    template_name = 'admintemplates/admineditoradd.html'
    model = Editor
    form_class = EditorForm
    context_object_name = 'admineditorcreate'
    success_url = reverse_lazy('newsapp:editorlist')


class EditorUpdate(UpdateView):
    template_name = 'admintemplates/admineditorupdate.html'
    model = Editor
    fields = ["user",
              "full_name", "contact_no", "address", "email", "image", "about"]
    tform_class = EditorForm
    success_url = reverse_lazy('newsapp:editorlist')

class EditorDelete(DeleteView):
    template_name = 'admintemplates/admineditorlist.html'
    model = Editor
    success_url = reverse_lazy('newsapp:editorlist')





# client views
# client views
# client views
# client views


class ClientHomeView(ListView):
    template_name = 'clienttemplates/clienthome.html'
    model = NewsCategory
    context_object_name = 'clientcategorylist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newslist'] = News.objects.all()
        return context
