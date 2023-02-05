from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница проекта Yatube')

def group_posts(request, slug):
    return HttpResponse(f'Cтраница, на которой будут посты, отфильтрованные по группам.')