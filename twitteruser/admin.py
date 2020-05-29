from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import tweeter, tweet, notifications


admin.site.register(tweeter, UserAdmin)
admin.site.register(tweet)
admin.site.register(notifications)
