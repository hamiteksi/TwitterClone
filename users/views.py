from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.db.models import Q
from django.contrib import messages
from tweets.models import TweetPost, Friends
# from django.contrib.auth.decorators import login_required
import random

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            redirect('/')


def signup(request):
    template = 'signup.html'
    if request.user.is_authenticated:
        return redirect('/')

    context = {}

    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        error = False
        if password1 != password2:
            messages.warning(request, 'Sifreler uyusmuyor')
            error = True
        if User.objects.filter(email=email).count():
            messages.warning(request, 'Bu email zaten var')
            error = True
        if User.objects.filter(username = username).count():
            messages.warning(request, 'Bu kullanici adinda biri var')
            error = True

        if error:
            return redirect('/user/signup/')

        User.objects.create_user(
            username = username,
            password = password1,
            email= email,
        )

        user = authenticate(
            username=username,
            password=password1,
        )
        if user is not None:
            login(request, user)
            messages.success(
                request,
                'Kullanici olusturma basarili.'
            )

            return redirect('/')

    return render(request, template, context)

def user_profile(request, user_name):
    context = {}
    profile = User.objects.get(username = user_name)

    if TweetPost.objects.filter(user = profile).count() == 0:
        messages.warning(
            request,
            'Bu kullanici henuz bir twit atmadi'
        )
    else:
        tweets = TweetPost.objects.filter(user = profile).order_by('-pk')
        context['tweets'] = tweets

    if request.POST.get('follow'):
        Friends.make_friend(request.user, profile)

    elif request.POST.get('unfollow'):
        Friends.remove_friend(request.user, profile)

    liste = [i for i in random.sample(list(User.objects.all()), 3) if i != request.user]

    context['liste'] = liste
    context['who_is'] = request.user.username
    context['profile'] = profile
    context['friend_check'] = Friends.objects.all()[0].follows.all()

    return render(request, 'user_index.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')