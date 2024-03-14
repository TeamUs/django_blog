from modeltranslation.translator import register, TranslationOptions
from .models import Post, JobSearch, SkillDevelopment, ProfessionalGrowth, ExpertInterview, ITNews, Connect


@register(Post)
class Post(TranslationOptions):
    fields = ("body", "title")


@register(JobSearch)
class JobSearch(TranslationOptions):
    fields = ("body", "title")


@register(SkillDevelopment)
class SkillDevelopment(TranslationOptions):
    fields = ("body", "title")


@register(ProfessionalGrowth)
class ProfessionalGrowth(TranslationOptions):
    fields = ("body", "title")


@register(ExpertInterview)
class ExpertInterview(TranslationOptions):
    fields = ("body", "title")


@register(ITNews)
class ITNews(TranslationOptions):
    fields = ("body", "title")


@register(Connect)
class Connect(TranslationOptions):
    fields = ("body", "title")
