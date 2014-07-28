from django.shortcuts import render
from django.views import generic
from . import models

class ArticleIndex(generic.ListView):
    queryset = models.Article.objects.published()
    template_name = "home.html"
    paginate_by = 2
