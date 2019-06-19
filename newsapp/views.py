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
from django.http import JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.conf import settings
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


# class EditorNewsDetailView(DetailView):
#     template_name = "admintemplates/editornewsdetail.html"
#     model = NewsCategory
#     context_object_name = 'newsdetail'


class EditorNewsCreate(EditorRequiredMixin, CreateView):
    template_name = 'admintemplates/editornewsadd.html'
    model = News
    form_class = EditorNewsForm
    context_object_name = 'newscreate'
    success_url = reverse_lazy('newsapp:newslist')


class EditorNewsUpdate(EditorRequiredMixin, UpdateView):
    template_name = 'admintemplates/editornewsupdate.html'
    model = News
    fields = ['title', 'main_category', 'sub_category',
              'image', 'video_link', 'content']
    template_name_suffix = '_form'
    success_url = reverse_lazy('newsapp:newslist')


class EditorNewsDelete(EditorRequiredMixin, DeleteView):
    template_name = 'admintemplates/editornewsdetail.html'
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
# Admin Views
# Admin Views

class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.groups.filter(name="Admin").exists():
            pass
        else:
            return redirect("/login/")
        return super().dispatch(request, *args, **kwargs)


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
        context['maincategorylist'] = NewsCategory.objects.all()
        context['topviewednews'] = News.objects.order_by('view_count')
        context['popularnews'] = News.objects.order_by('-view_count')
        context['hotnews'] = News.objects.order_by('created_at')
        context['mostcommented'] = Comment.objects.order_by('-comment')
        context['newseditor'] = Editor.objects.all()
        context['advertiselist'] = Advertizement.objects.all()
        context['subform'] = SubscriberForm
        return context


class ClientNewsDetailView(DetailView):
    template_name = 'clienttemplates/clientnewsdetail.html'
    model = News
    context_object_name = 'clientnewsdetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertiselist'] = Advertizement.objects.all()
        context['popularnews'] = News.objects.order_by('-view_count')
        context['mostcommented'] = Comment.objects.order_by('-comment')
        context['newseditor'] = Editor.objects.all()
        return context


class SubscriberView(SuccessMessageMixin, CreateView):
    template_name = "clienttemplates/error.html"
    form_class = SubscriberForm
    success_url = reverse_lazy('newsapp:home')
    success_message = "thank you for subscribing"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        if Subscriber.objects.filter(email=email).exists():
            return render(self.request, ("clienttemplates/error.html"), {"error": "subscriber already exist"})
        send_mail("Subscription mail", "Thank you for Subscribing our news site",
                  settings.EMAIL_HOST_USER, [email, ], fail_silently=False),
        return super().form_valid(form)


class SubscriberCheckView(View):
    def get(self, request):
        email = request.GET.get("email")
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({"error": "error"})
        else:
            return JsonResponse({"error": "success"})
