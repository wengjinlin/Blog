# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('summary', models.CharField(max_length=255)),
                ('read_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('up_count', models.IntegerField(default=0)),
                ('down_count', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('article_type', models.IntegerField(choices=[(1, 'Python'), (2, 'Linux'), (3, 'OpenStack'), (4, 'GoLang')], default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Article2Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='repository.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('site', models.CharField(max_length=32, unique=True)),
                ('theme', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='repository.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='repository.Article')),
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back', to='repository.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='repository.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='UpDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article')),
            ],
        ),
        migrations.CreateModel(
            name='UserFans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('nickname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avatar', models.ImageField(upload_to='')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('fans', models.ManyToManyField(through='repository.UserFans', to='repository.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='userfans',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='userfans',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='updown',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='article2tag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='repository.Blog'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='repository.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='repository.Article2Tag', to='repository.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='userfans',
            unique_together=set([('user', 'follower')]),
        ),
        migrations.AlterUniqueTogether(
            name='updown',
            unique_together=set([('article', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='article2tag',
            unique_together=set([('article', 'tag')]),
        ),
    ]
