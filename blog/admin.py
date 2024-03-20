from django.contrib import admin
from .models import Post, JobSearch, SkillDevelopment, ProfessionalGrowth,ExpertInterview,ITNews
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(Post) #Регистрация модели нашего поста
admin.site.register(JobSearch)
admin.site.register(SkillDevelopment)
admin.site.register(ProfessionalGrowth)
admin.site.register(ExpertInterview)
admin.site.register(ITNews)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'description', 'age', 'gender')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'description', 'age', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)