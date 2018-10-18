# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.http import HttpResponseRedirect, Http404  # HttpResponse
from django.contrib import messages


# Create your views here.
def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    if not request.user.is_authenticated():
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "item Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Error enter data again")
    context = {
        "form": form,
    }
    return render(request, "form.html", context)


def main_page(request):
    query_list = Post.objects.filter(wait=False)[:3]
    context = {
        'posts': query_list,
    }
    return render(request, "index.html", context)


def post_list(request):
    query_list_posts = Post.objects.filter(wait=False)
    paginator = Paginator(query_list_posts, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger or EmptyPage:
        contacts = paginator.page(1)
    context = {
        'contacts': contacts,
        # 'form': PostForm
    }
    return render(request, "list.html", context)


def about(request):
    return render(request, "about.html")


def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,

    }
    return render(request, "post.html", context)

