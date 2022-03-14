from statistics import mode
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post

# Create your views here.
class index(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']