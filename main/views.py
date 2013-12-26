# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from blog.models import Post
from review.models import *
# from slider.models import Slider
# from game.models import Game
# from user_profile.models import Supernumerary


class MainView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context

class SaitView(TemplateView):
    template_name = 'sait.html'

    def get_context_data(self, **kwargs):
        context = super(SaitView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context

class MobileView(TemplateView):
    template_name = 'mobile.html'

    def get_context_data(self, **kwargs):
        context = super(MobileView, self).get_context_data()
        context['posts'] = Post.objects.all()
        context['reviews'] = Review.objects.all()
        # context['slides'] = Slider.objects.all()
        # context['games'] = Game.objects.all()
        # context['supernumeraries'] = Supernumerary.objects.all()
        return context