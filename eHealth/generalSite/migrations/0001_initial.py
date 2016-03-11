# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contract_email', models.EmailField(max_length=75)),
                ('hours', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('sitename', models.CharField(max_length=100)),
                ('sitelogo', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_public', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Favorite_Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linkURL', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('visits', models.PositiveIntegerField(default=0)),
                ('summary', models.CharField(max_length=1000)),
                ('flesch_score', models.PositiveIntegerField()),
                ('polarity_score', models.PositiveIntegerField()),
                ('subjectivity_score', models.PositiveIntegerField()),
                ('category', models.ForeignKey(to='generalSite.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Saved_Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_public', models.BooleanField(default=False)),
                ('link', models.OneToOneField(to='generalSite.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Searcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=40)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=75)),
                ('name', models.CharField(max_length=1000)),
                ('surname', models.CharField(max_length=1000)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=6, choices=[(b'Other', b'Other'), (b'Male', b'Male'), (b'Female', b'Female')])),
                ('searcher', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='search',
            name='user',
            field=models.ForeignKey(to='generalSite.Searcher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saved_page',
            name='user',
            field=models.ForeignKey(to='generalSite.Searcher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorite_search',
            name='query',
            field=models.OneToOneField(to='generalSite.Search'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorite_search',
            name='user',
            field=models.ForeignKey(to='generalSite.Searcher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category_list',
            name='user',
            field=models.ForeignKey(to='generalSite.Searcher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='category_list',
            field=models.ForeignKey(to='generalSite.Category_List'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(to='generalSite.Searcher'),
            preserve_default=True,
        ),
    ]
