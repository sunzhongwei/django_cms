# -*- coding: utf-8 -*-

from django.db import models

class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # Slug is a newspaper term. A slug is a short label for something,
    # containing only letters, numbers, underscores or hyphens. They’re
    # generally used in URLs.
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    objects = ArticleQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "CMS Article"
        verbose_name_plural = "CMS Articles"
        ordering = ["-created_at", ]

