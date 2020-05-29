from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),
    path('profile/<user>/', views.profile),
    path('tweeter/<user>/', views.tweeter_profile),
    path('post_tweet/<user>/', views.tweet_view),
    path('notifications/<user>/', views.notifications),
]
