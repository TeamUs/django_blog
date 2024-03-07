from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=450) #Заголовок поста
    author = models.ForeignKey( #Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE, #Удаление поста
    )
    body = models.TextField() #Поле нашего поста

    def __str__(self): #Метод
        return self.title

class JobSearch(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class SkillDevelopment(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProfessionalGrowth(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ExpertInterview(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ITNews(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Connect(models.Model):
    title = models.CharField(max_length=450)
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
