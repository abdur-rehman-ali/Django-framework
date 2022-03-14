from statistics import mode
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.
class index(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']

class postDetail(DetailView):
    model = Post
    template_name = 'updatePost.html'
    