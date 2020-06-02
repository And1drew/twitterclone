from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitteruser.models import tweet, tweeter, notifications
from twitteruser.forms import login_form, signup_form, tweet_form
# Create your views here.


@login_required
def index(request):
    data = tweet.objects.all()
    return render(request, "index.html", {"tweets": data})


def signin(request):
    form = login_form(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(
            request, username=data['username'], password=data['password']
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    form = login_form()
    return render(request, 'signin.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweeter.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password'],
            )
            return HttpResponseRedirect('/signin')
    form = signup_form()
    return render(request, "signup.html", {'form': form})


def signout(request):
    logout(request)
    return HttpResponseRedirect('/signin')


def profile(request, user):
    form = tweet.objects.filter(author=request.user)
    return render(request, "profile.html", {"tweets": form})


def tweeter_profile(request, user):
    if not user:
        user = tweeter.objects.filter(username=user)
        user = user.first()
    tweeter_info = tweeter.objects.filter(username=user)
    tweeter_info = tweeter_info.first()
    form = tweet.objects.filter(author=request.user)
    return render(request, "tweeter_profile.html",
                  {"tweeter": tweeter_info, "tweets": form})


def tweet_view(request, user):
    if request.method == "POST":
        form = tweet_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet.objects.create(
                author=request.user,
                description=data['description'],
            )
            return HttpResponseRedirect('/')
    form = tweet_form()
    return render(request, "post_tweet.html", {'form': form})


def notifications_view(request):
    form = notifications.objects.all()
    return render(request, "notifications.html", {"notifications": form})
