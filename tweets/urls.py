from django.urls import path
from . import views

urlpatterns = [
    path('tweet/', views.tweet, name='tweet'),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.welcome, name='anasayfa'),
#     path('user/', include('user_profile.urls')),
#
#     # path('logout/', views.logout_view, name='logout'),
#     # path('index/', views.index, name='user_index'),
#     # path('login/', auth_views.LoginView.as_view(template_name='./login.html'), name='login'),
#     # path('signup/', views.signup, name='signup'),
#     # path('u/<slug:user_name>/', views.user_profile, name = 'user_details'),
#     # path('u/<slug:user_name>/follow/', views.add_follows, name='followed'),
# ]

