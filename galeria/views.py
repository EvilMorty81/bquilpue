from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
"""def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'galeria/index.html', {})"""
def index(request):
    return render(request, 'galeria/index.html')

def galeria(request):
    return render(request, 'galeria/galeria.html')

def formulario(request):
    return render(request, 'galeria/formulario.html')

@login_required(login_url="/login/")
def galeria_create(request):
    return render(request, 'galeria/galeria_create.html')