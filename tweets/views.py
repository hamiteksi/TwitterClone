from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from tweets.models import TweetPost, Friends
from django.contrib.auth.decorators import login_required
# import random

@login_required
def tweet(request):
    context = {}
    if request.method == "POST":
        sent = request.POST.get('tweet')
        print(sent)
        created_tweet = TweetPost.objects.create(
        user=request.user,
        post=sent,
    )

    if created_tweet:
        messages.success(request, 'Tweet Added')

    return redirect('/')
    # posts = Q()
    # # for authors in Friends.objects.all()[0].follows.all():
    # #     posts = posts | Q(authors=authors)


