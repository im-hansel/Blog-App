from django.shortcuts import render, get_object_or_404
from .models import Blog

def index(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, 'blogapp/index.html', context)

def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {"blog": blog}
    return render(request, 'blogapp/detail.html', context)
