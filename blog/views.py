from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, JobSearch, SkillDevelopment, ProfessionalGrowth, ExpertInterview, ITNews, Connect

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

