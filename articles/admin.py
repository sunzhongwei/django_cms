# -*- coding: utf-8 -*-
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from . import models

class ArticleAdmin(MarkdownModelAdmin):
    list_display = ("title", "created_at")
    # Adding a ManyToManyField to this list will instead use a nifty
    # unobtrusive JavaScript “filter” interface that allows searching within
    # the options.
    filter_horizontal = ("tags", )

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tag)
