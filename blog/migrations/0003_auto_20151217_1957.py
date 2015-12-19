# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
