from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Post(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()


class JobSearch(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SkillDevelopment(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ProfessionalGrowth(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class ExpertInterview(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ITNews(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class Connect(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    class Meta:
        swappable = 'AUTH_USER_MODEL'
