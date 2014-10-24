# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from blog.views import AuthorBlog, AuthorBlogDetail


urlpatterns = patterns('',
    url(r'^$', AuthorBlog.as_view(), name='author'),
    url(r'^(?P<slug>[-_\w]+)/$', AuthorBlogDetail.as_view(), name='detail_author_blog'),
)
