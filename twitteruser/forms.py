from django import forms
# from twitteruser.models import tweeter


class login_form (forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class signup_form (forms.Form):
    username = forms.CharField(max_length=50)
    displayname = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class tweet_form(forms.Form):
    # author = forms.ModelChoiceField(queryset=tweeter.objects.all())
    description = forms.CharField(max_length=140)
