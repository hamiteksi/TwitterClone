from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from tweets.models import TweetPost, Friends
from django.contrib.auth.decorators import login_required
import random

@login_required
def index(request):
    context = dict()
    tweets = TweetPost.objects.filter(
        user__in=Friends.objects.all()[0].follows.all()).order_by('-pk')

    context['tweets'] = tweets
    context['who_is'] = request.user.username
    liste = [i for i in random.sample(list(User.objects.exclude(id=request.user.id)), 3)
             if i != request.user]

    context['liste'] = liste
    return render(request, 'index.html', context)


def welcome(request):
    context = {}
    context['title'] = 'Twittera hosgeldin!'
    template = 'welcome.html'
    if request.user.is_authenticated:
        return redirect('/index')

    return render(request, template, context)



