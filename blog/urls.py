from .views import Bloglist, BlogDetailView, AboutPageView, JobSearchListView, SkillDevelopmentListView, ProfessionalGrowthListView, ExpertInterviewListView, ITNewsListView, ConnectListView, InterviewDetailListView
from django.contrib.auth.views import LogoutView

from .views import RegisterUserView, LoginUserView
from django.urls import path, include
from .views import ProfileView, ProfileEditView
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
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('i18n/', include("django.conf.urls.i18n")),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('register/', RegisterUserView.as_view(), name='register'),
]