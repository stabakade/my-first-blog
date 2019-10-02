from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from . import forms
from .serialisers import BlogSerializer
from rest_framework import generics
from .models import Post
from rest_framework import viewsets
# Create your views here.


class BlogViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class BlogList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  #in case we get a pk which is not defined yet
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

