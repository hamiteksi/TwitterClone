from django.contrib import admin
from .models import TweetPost, Friends

# Register your models here.

admin.site.register(TweetPost)
admin.site.register(Friends)