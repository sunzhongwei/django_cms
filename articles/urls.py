# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns("",
    url(r"^(?P<article_id>\d+)/.*$", views.detail, name="detail"),
    url(r"^$", views.index, name="index"),
)
