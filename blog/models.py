from django.db import models

class Post(models.Models):
    title = models.CharField(max_length=100)    # Заголовок поста
    content = models.TextField()                # Контент поста
    created_at = models.DateTimeField(auto_now_add=True)    # Для создания

    def __str__(self):
        return self.title
        
