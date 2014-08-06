from django.shortcuts import render, get_object_or_404
from . import models

def index(request):
    articles = models.Article.objects.order_by("-id")[:5]
    context = {"articles": articles}
    return render(request, "articles/home.html", context)

def detail(request, article_id):
    article = get_object_or_404(models.Article, pk=article_id)
    context = {"article": article}
    return render(request, "articles/detail.html", context)
