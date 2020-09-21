from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category, Dairy, Message, Proflie, comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import auth
from DjangoUeditor.models import UEditorField


# Create your views here.


# 博客首页
def index(request):
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    # 把查询出来的分类封装到上下文里
    return render(request, 'index.html', locals())


# 文章首页
def blog(request):
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    star = Article.objects.filter(star__id=1)[:3]  # 查询推荐位ID为1的文章
    allacrticles = Article.objects.all().order_by('-id')  # 查询所有文章
    newarticle = Article.objects.all().order_by('-id')[0:5]  # 查询所有文章中最新的5篇

    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(allacrticles, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        allacrticles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        allacrticles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        allacrticles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request, 'blog.html', locals())


# 列表页
def list(request, lid):
    newarticle = Article.objects.all().order_by('-id')[0:5]  # 查询所有文章中最新的5篇
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    selectedcategory = Category.objects.get(id=lid)
    star = Article.objects.filter(star__id=1)[:3]  # 查询推荐位ID为1的文章
    list = Article.objects.filter(category_id=lid)  # 获取通过URL传进来的lid，然后筛选出对应文章
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    # 把查询出来的分类封装到上下文里
    return render(request, 'list.html', locals())


# 内容页
def read(request, sid):
    read = Article.objects.get(id=sid)
    previous_blog = Article.objects.filter(created_time__gt=read.created_time).first()
    next_blog = Article.objects.filter(created_time__lt=read.created_time).last()
    read.views = read.views + 1
    cmts = comments.objects.filter(article=sid)
    read.save()
    return render(request, 'read.html', locals())


# 标签页
def tag(request, tag):
    newarticle = Article.objects.all().order_by('-id')[0:5]  # 查询所有文章中最新的5篇
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    star = Article.objects.filter(star__id=1)[:3]  # 查询推荐位ID为1的文章
    list = Article.objects.filter(tags__name=tag)  # 获取通过URL传进来的lid，然后筛选出对应文章
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    # 把查询出来的分类封装到上下文里
    return render(request, 'Tag.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    newarticle = Article.objects.all().order_by('-id')[0:5]  # 查询所有文章中最新的5篇
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    star = Article.objects.filter(star__id=1)[:3]  # 查询推荐位ID为1的文章
    allArticle = Article.objects.all()
    list = []
    for x in allArticle:
        if ss in x.title:
            list.append(x)
        elif ss in x.body:
            list.append(x)
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    # 把查询出来的分类封装到上下文里
    return render(request, 'search.html', locals())


# 关于我们
def Link(request):
    return render(request, 'link.html')


def diary(request):
    dary = Dairy.objects.all()
    return render(request, 'diary.html', locals())


def message(request):
    if request.method == 'POST':
        msg = request.POST.get("body")
        mesg = Message()
        mesg.body = msg
        mesg.user = request.user
        mesg.save()

        return redirect('message')

    cnts = Message.objects.all()
    context = {'cnts': cnts}
    return render(request, 'message.html', context)


def log_in(request):
    if request.method == 'POST':
        user_name = request.POST.get("username")
        pwd = request.POST.get("pwd")
        user = auth.authenticate(username=user_name, password=pwd)
        if user:
            auth.login(request, user)
            return redirect('blog.html')
        else:
            return HttpResponse("账号或密码输入有误,请重新输入")

    return render(request, 'login.html')


def log_out(request):
    auth.logout(request)
    return redirect("index")


def register(request):
    error = " "
    if request.method == 'POST':
        user_name = request.POST.get("username")
        pass_word_1 = request.POST.get("pwd_1")
        pass_word_2 = request.POST.get("pwd_2")
        mail = request.POST.get("email")
        if User.objects.filter(username=user_name):
            error = "用户已存在"


        elif pass_word_1 != pass_word_2:
            error = "两次密码请输入一致"

        elif not pass_word_1 or not pass_word_1:
            error = "密码不能为空"

        elif not user_name or not mail:
            error = "用户名与邮箱不能为空"

        else:
            User.objects.create_user(username=user_name, password=pass_word_1, email=mail)
            return render(request, 'login.html')

    return render(request, "register.html", {"error_message": error})


def editprofile(request, id):
    user = User.objects.get(id=id)
    # user_id是OneToOneField自动生成的字段
    profile = Proflie.objects.get(user_id=id)
    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("你没有权限修改次用户信息")
        ph = request.POST.get("phone")
        fa = request.POST.get("favor")
        ste = request.POST.get("stella")
        bir = request.POST.get("birth")
        slfi = request.POST.get("selfintro")
        if not ph or not fa or not ste or not bir or not slfi:
            return HttpResponse("输入框不能为空!")
        else:
            profile.phone = ph
            profile.favor = fa
            profile.constellation = ste
            profile.birth = bir
            profile.self_intro = slfi
            profile.save()

        return render(request, 'UserProfile.html', locals())

    return render(request, 'UserProfile.html', locals())


def article_comment(request, aid):
    article = get_object_or_404(Article, id=aid)
    if request.method == 'POST':
        cmt = request.POST.get("body")
        comts = comments()
        comts.user = request.user
        comts.article = article
        comts.body = cmt
        comts.save()

        return redirect(article)

    return render(request, 'read.html')
