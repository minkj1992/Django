from django.shortcuts import render

from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html',{'posts':posts})