from django.shortcuts import render
from .models import Post  # импорт модели

# Create your views here.

def post_list(request):
    posts = Post.objects.all()                                          # получаем все записи из модели Post
    print("Посты:", posts)                                              # выводим список постов в консоль
    return render(request, 'blog/post_list.html', {'posts': posts})     # передаем их в шаблон
