from django.urls import path
from . import views

app_name = 'ml'

urlpatterns = [
    path('choose_model/', views.choose_model, name='choose_model'),
]

