from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def mainsite_index(request):
    posts = Post.objects.all()
    li = list()
    for count, value in enumerate(posts):
        li.append(f'No.{count}:{value}<br/>')
    return HttpResponse(li)
