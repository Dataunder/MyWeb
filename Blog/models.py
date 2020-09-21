from django.db import models
from django.urls import reverse

from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# 推荐位
class Star(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章分类
class Category(models.Model):
    name = models.CharField('分类名', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '分类名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField('标签名', max_length=100)

    class Meta:
        verbose_name = '标签名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 作者
class Auth(models.Model):
    auth_name = models.CharField('作者名', max_length=20)

    class Meta:
        verbose_name = '作者名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.auth_name


# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', blank=True, null=True)
    # 文章与分类是一对多的关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 文章与标签多对多的关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    body = UEditorField('内容', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE, verbose_name='作者名')
    # 文章和作者是一对多的关系
    star = models.ForeignKey(Star, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)

    views = models.PositiveIntegerField('阅读量', default=0)

    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    urls = models.URLField('网址', max_length=100)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('read', args=[self.id])


# 友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'


class Dairy(models.Model):
    name = models.CharField('日记', max_length=20)
    msg = models.TextField('日记内容', max_length=100)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '日记'
        verbose_name_plural = '日记'


class Proflie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='proflie')
    phone = models.CharField('电话', max_length=20, blank=True)
    favor = models.CharField('爱好', max_length=10, blank=True)
    constellation = models.CharField('星座', max_length=6, blank=True)
    birth = models.CharField('生日', max_length=20, blank=True)
    self_intro = models.CharField('自我介绍', max_length=50, blank=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)

    class Meta:
        verbose_name = '资料'
        verbose_name_plural = '资料'


@receiver(post_save, sender=User)
def create_user_proflie(sender, instance, created, **kwargs):
    if created:
        Proflie.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_proflie(sender, instance, **kwargs):
    instance.proflie.save()


class Message(models.Model):
    body = models.TextField('留言内容', max_length=100)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    user = models.ForeignKey(
        User,
        verbose_name='用户',
        on_delete=models.CASCADE,
        related_name='Msg',
    )

    class Meta:
        verbose_name = '留言板'
        verbose_name_plural = '留言板'

    def __str__(self):
        return self.body[:20]


class comments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='用户',
        on_delete=models.CASCADE,
        related_name='cmt',
    )

    article = models.ForeignKey(
        Article,
        verbose_name='文章',
        on_delete=models.CASCADE,
        related_name='cmt',
    )
    body = models.TextField('留言内容', max_length=100)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = '文章留言'
        verbose_name_plural = '文章留言'

    def __str__(self):
        return self.body[:20]
