from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, JobSearch, SkillDevelopment, ProfessionalGrowth, ExpertInterview, ITNews, Connect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ProfileEditForm


class Bloglist(ListView):
    model = Post
    paginate_by = 3
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class JobSearchListView(ListView):
    model = JobSearch
    paginate_by = 3
    template_name = 'job_search_list.html'
    context_object_name = 'job_search_list'

class SkillDevelopmentListView(ListView):
    model = SkillDevelopment
    paginate_by = 3
    template_name = 'skill_development_list.html'
    context_object_name = 'skill_development_list'

class ProfessionalGrowthListView(ListView):
    model = ProfessionalGrowth
    paginate_by = 3
    template_name = 'professional_growth_list.html'
    context_object_name = 'professional_growth_list'

class ExpertInterviewListView(ListView):
    model = ExpertInterview
    paginate_by = 3
    template_name = 'expert_interview_list.html'
    context_object_name = 'expert_interview_list'

class InterviewDetailListView(DetailView):
    model = ExpertInterview
    template_name = 'interview_detail.html'
    context_object_name = 'expert_interview'

class ITNewsListView(ListView):
    model = ITNews
    paginate_by = 3
    template_name = 'it_news_list.html'
    context_object_name = 'it_news_list'

class ConnectListView(ListView):
    model = Connect
    template_name = 'connect.html'
    context_object_name = 'posts'

class RegisterUserView(FormView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        User.objects.create_user(username=username, password=password)
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return super().form_valid(form)

class LoginUserView(FormView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')  # Укажите URL для перехода после успешной аутентификации

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)



class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        form = ProfileEditForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

class ProfileEditView(LoginRequiredMixin, View):
    template_name = 'profile_edit.html'

    def get(self, request, *args, **kwargs):
        form = ProfileEditForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})