from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


# from tweets.views import tweet

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='./login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('u/<slug:user_name>/', views.user_profile, name = 'user_details'),
    # path('u/<slug:user_name>/follow/', views.add_follows, name='followed'),
]
