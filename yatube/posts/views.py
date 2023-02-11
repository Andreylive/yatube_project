from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = 'posts/index.html'
    title = 'Проект Yatube'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text,
        }
    return render(request, template, context) 

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Проект Yatube'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
        }
    return render(request, template, context)