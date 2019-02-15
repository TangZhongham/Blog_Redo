from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    num = 10
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')[:num]
    return render(request, 'blog/archives.html', context={'date_list': post_list})


def listing(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list, 3) # 每页显示 3 个联系人

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        post_list = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'post_list': post_list})

