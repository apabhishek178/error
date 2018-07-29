from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView

from .views import (
    TweetListAPIView,
    TweetCreateAPIView
    )

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name="list"),
    url(r'^create/', TweetCreateAPIView.as_view(), name="create"),
    ]

