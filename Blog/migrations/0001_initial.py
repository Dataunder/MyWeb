# Generated by Django 3.1 on 2020-09-20 11:34

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('excerpt', models.TextField(blank=True, max_length=200, verbose_name='摘要')),
                ('img', models.ImageField(blank=True, null=True, upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片')),
                ('body', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('urls', models.URLField(max_length=100, verbose_name='网址')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=20, verbose_name='作者名')),
            ],
            options={
                'verbose_name': '作者名',
                'verbose_name_plural': '作者名',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名')),
                ('index', models.IntegerField(default=999, verbose_name='分类排序')),
            ],
            options={
                'verbose_name': '分类名',
                'verbose_name_plural': '分类名',
            },
        ),
        migrations.CreateModel(
            name='Dairy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='日记')),
                ('msg', models.TextField(max_length=100, verbose_name='日记内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '日记',
                'verbose_name_plural': '日记',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='链接名称')),
                ('linkurl', models.URLField(max_length=100, verbose_name='网址')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='推荐位')),
            ],
            options={
                'verbose_name': '推荐位',
                'verbose_name_plural': '推荐位',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签名',
                'verbose_name_plural': '标签名',
            },
        ),
        migrations.CreateModel(
            name='Proflie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='电话')),
                ('favor', models.CharField(blank=True, max_length=10, verbose_name='爱好')),
                ('constellation', models.CharField(blank=True, max_length=6, verbose_name='星座')),
                ('birth', models.CharField(blank=True, max_length=20, verbose_name='生日')),
                ('self_intro', models.CharField(blank=True, max_length=50, verbose_name='自我介绍')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proflie', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '资料',
                'verbose_name_plural': '资料',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=100, verbose_name='留言内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Msg', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '留言板',
                'verbose_name_plural': '留言板',
            },
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=100, verbose_name='留言内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmt', to='Blog.article', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmt', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '文章留言',
                'verbose_name_plural': '文章留言',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.auth', verbose_name='作者名'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='star',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Blog.star', verbose_name='推荐位'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Blog.Tag', verbose_name='标签'),
        ),
    ]