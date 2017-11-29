# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 18:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0005_auto_20171125_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('parent_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='ID родительского комментария')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('is_moderated', models.BooleanField(default=True, verbose_name='Одобрено модератором')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Комментарий отображается как удаленный')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AlterModelOptions(
            name='binarypost',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='textpost',
            options={'verbose_name': 'Текстовый пост', 'verbose_name_plural': 'Текстовые посты'},
        ),
        migrations.AlterField(
            model_name='binarypost',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='binarypost',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='category',
            name='kind',
            field=models.CharField(choices=[('0', 'Файлы'), ('1', 'Посты'), ('3', 'Не определено')], default='3', help_text='<font color="red">Внимание! Изменение этого поля у существующих категорий может повлиять на отображение объектов!</font>', max_length=254, verbose_name='Тип объектов'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='route',
            field=models.CharField(max_length=200, verbose_name='Название в URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_moderated',
            field=models.BooleanField(default=True, verbose_name='Одобрено модератором'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='textpost',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Post', verbose_name='ID поста'),
        ),
    ]