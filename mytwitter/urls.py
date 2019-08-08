from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='anasayfa'),
    path('user/', include('users.urls')),
    path('index/', views.index, name='user_index'),
    path('tweet/', include('tweets.urls')),

]

