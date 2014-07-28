from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from . import models

class ArticleAdmin(MarkdownModelAdmin):
    list_display = ("title", "created_at")

admin.site.register(models.Article, ArticleAdmin)
