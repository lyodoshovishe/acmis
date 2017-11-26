from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone

from .models import Post, Category
from .forms import TextPostForm, BinaryPostForm, PostForm

def post_list(request, tags=None, category=None, author=None):

  t = c = None
  if category:
    c = get_object_or_404(Category, route=category)

  if tags:
    t = tags.split(",")

  query = {
    'is_public': True,
    'tags_in_name': t,
    'author__username': author,
    'category': c,
  }

  q = {k: v for k, v in query.items() if v is not None}

  posts = Post.objects.filter(**q).distinct()

  return render(request, 'cms/post_list.html', {'posts': posts, 'category': category})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'cms/post_detail.html', {'post': post})

def post_new(request,category):
  categoryObj = Category.objects.get(route=category)

  if categoryObj.kind == '0':
    formClass = BinaryPostForm
  elif categoryObj.kind == '1':
    formClass = TextPostForm
  else:
    formClass = PostForm

  if request.method == "POST":
    form = formClass(request.POST, request.FILES)

    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.category = categoryObj

      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = formClass()

  return render(request, 'cms/post_edit.html', {'form': form})

def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)

  if post.category.kind == '0':
    formClass = BinaryPostForm
  elif post.category.kind == '1':
    formClass = TextPostForm
  else:
    formClass = PostForm

  if request.method == "POST":
    print(request.POST)
    print(request.FILES)
    form = formClass(request.POST, request.FILES, instance=post)

    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()

      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = formClass(instance=post)

  return render(request, 'cms/post_edit.html', {'form': form})
