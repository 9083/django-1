from django.contrib import admin
from .models import Post        # импорт модели

admin.site.register(Post)       # регистрируем модель в админке

# Register your models here.
