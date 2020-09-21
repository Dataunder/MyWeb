"""MyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from Blog import views
from django.views.static import serve
from MyWeb import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    path('', views.index, name='index'),  # 网站首页
    path('index.html', views.index, name='index'),  # 网站首页
    path('blog.html', views.blog, name='blog'),  # 列表页
    path('list-<int:lid>.html', views.list, name='list'),  # 列表页
    path('read-<int:sid>.html', views.read, name='read'),  # 内容页
    path('tag/<tag>', views.tag, name='tags'),  # 标签列表页
    path('s/', views.search, name='search'),  # 搜索列表页
    path('link.html', views.Link, name='link'),  # 友情链接页
    path('diary.html', views.diary, name='diary'),  # 日记页
    path('message.html', views.message, name='message'),  # 留言页
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('register.html', views.register, name='register'),
    path('UserProfile-<int:id>', views.editprofile, name='profile'),
    path('Art_cmt-<int:aid>',views.article_comment,name='Artc')
]
