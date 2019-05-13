# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-05-09 23:29
from __future__ import unicode_literals

import cms.utils
from django.db import migrations, models

def populate_value(apps, schema_editor):
    cmspost = apps.get_model('cms', 'cmspost')
    for row in cmspost.objects.all():
        if row.is_public and row.is_moderated:
            row.publish_date = row.created_date
        row.save(update_fields=['publish_date'])

class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20181229_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmspost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='is_moderated',
            field=models.BooleanField(default=True, help_text='Якщо не відмічено, то пост не буде відображатися', verbose_name='Підтвердити оприлюднення'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='is_public',
            field=models.BooleanField(default=True, help_text='Якщо не відмічено, то пост буде збережено як чернетка', verbose_name='Оприлюднити'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=cms.utils.PathAndRename('avatars/'), verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_moderated',
            field=models.BooleanField(default=True, help_text='Якщо не відмічено, то комментар не буде відображатися', verbose_name='Підтвердити оприлюднення'),
        ),

        migrations.RunPython(populate_value, reverse_code=migrations.RunPython.noop),
    ]