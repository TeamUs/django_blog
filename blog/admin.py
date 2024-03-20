from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, JobSearch, SkillDevelopment, ProfessionalGrowth, ExpertInterview, ITNews

admin.site.register(Post) # Регистрация модели нашего поста
admin.site.register(JobSearch)
admin.site.register(SkillDevelopment)
admin.site.register(ProfessionalGrowth)
admin.site.register(ExpertInterview)
admin.site.register(ITNews)

from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from .models import CustomUser

class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = CustomUser
        fields = '__all__'

# Ваш CustomUserAdmin будет выглядеть так:
class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    list_display = ('first_name', 'last_name', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

