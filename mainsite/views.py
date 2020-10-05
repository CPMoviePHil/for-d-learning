from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def mainsite_index(request):
    posts = Post.objects.all()
    # li = list()
    # for count, value in enumerate(posts):
    #     li.append(f'No.{count}:{value}<br/>')
    
    now = datetime.now()
    context = {
        'posts': posts,
        'now': now,
    }
    return render(request, 'mainsite/index.html', context)
