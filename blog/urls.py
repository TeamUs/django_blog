from .views import Bloglist, BlogDetailView, AboutPageView, JobSearchListView, SkillDevelopmentListView, \
    ProfessionalGrowthListView, ExpertInterviewListView, ITNewsListView, ConnectListView, InterviewDetailListView, \
    LoginAjaxView, RegisterAjaxView
from django.contrib.auth.views import LogoutView
from django.urls import path, include
urlpatterns = [
    path('post/<int:pk>',BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', Bloglist.as_view(), name='home'),
    path('job-search/', JobSearchListView.as_view(), name='job_search_list'),
    path('skill-development/', SkillDevelopmentListView.as_view(), name='skill_development_list'),
    path('professional-growth/', ProfessionalGrowthListView.as_view(), name='professional_growth_list'),
    path('expert-interview/', ExpertInterviewListView.as_view(), name='expert_interview_list'),
    path('interview_detail/<int:pk>/', InterviewDetailListView.as_view(), name='interview_detail_list'),
    path('it-news/', ITNewsListView.as_view(), name='it_news_list'),
    path('connect/', ConnectListView.as_view(), name='connect_list'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('i18n/', include("django.conf.urls.i18n")),
    path('register_ajax/', RegisterAjaxView.as_view(), name='register_ajax'),
    path('login_ajax/', LoginAjaxView.as_view(), name='login_ajax')
]