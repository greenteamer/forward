# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import *

class PostList(ListView):
    template_name = 'blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

class PostDetail(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class AuthorBlog(ListView):
    template_name = 'author_blog.html'
    context_object_name = 'author_posts'
    queryset = BlogPost.objects.all()

class AuthorBlogDetail(DetailView):
    model = BlogPost
    template_name = 'author_blog_detail.html'