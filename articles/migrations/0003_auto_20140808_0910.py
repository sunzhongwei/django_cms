# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to=b'articles.Tag'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
    ]
