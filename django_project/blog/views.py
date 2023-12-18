from django.shortcuts import render
from django.http import HttpResponse

posts = [{
    'author': 'pawan kumar',
    'title': 'blog post1',
    'content': 'first post content',
    'date_posted': 'may 5,2007'
},
    {
        'author': 'dinesh',
        'title': 'blog post2',
        'content': 'second post content',
        'date_posted': 'may 25,2008'
    }
]


def home(request):
    context ={'posts':posts}
    return render(request, 'blog/home.html', context)


def about(request):
    context ={'posts':posts}
    return render(request, 'blog/about.html', context)

