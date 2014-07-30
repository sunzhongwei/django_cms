from django.shortcuts import render
from . import models

def index(request):
    articles = models.Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/home.html", context)
