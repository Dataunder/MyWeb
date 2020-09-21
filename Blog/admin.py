from django.contrib import admin

from .models import Auth, Article, Category, Tag, Link, Star, Dairy, Proflie, Message,comments
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Register your models here.
# 在admin页面注册文章表方便编辑
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['title', 'category']
    list_display = ('title', 'created_time', 'modified_time', 'category', 'auth')
    fields = ['title', 'excerpt', 'body', 'category', 'tags', 'auth', 'star', 'urls']
    list_per_page = 20
    ordering = ('created_time',)
    search_fields = ['title', 'body', 'category__name', 'auth']


# 在admin页面注册分类表方便编辑
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')
    search_fields = ['name']


# 在admin页面注册标签表方便编辑
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


# 在admin页面注册链接表方便编辑
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')
    search_fields = ['name']


# 在admin页面注册作者表方便编辑
@admin.register(Auth)
class AuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'auth_name')
    search_fields = ['auth_name']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('body', 'created_time', 'user')


# 注册推荐表
@admin.register(Star)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


@admin.register(Dairy)
class DairyAdmin(admin.ModelAdmin):
    list_display = ('name', 'msg')
    search_fields = ['name', 'msg']

@admin.register(comments)
class commentsAdmin(admin.ModelAdmin):
    list_display = ('user','article','body')


class ProfileInline(admin.StackedInline):
    model = Proflie
    can_delete = False
    verbose_name_plural = 'UserProfile'


# 将Profile关联到User中
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# 重新注册User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
