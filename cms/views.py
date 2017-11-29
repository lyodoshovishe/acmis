from  hashlib import md5

from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, Http404

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Post, Category, Comment
from .forms import TextPostForm, BinaryPostForm, PostForm, CommentForm

#TODO move to user's part
from django.contrib.auth.signals import user_logged_in
def do_stuff(sender, user, request, **kwargs):
  maps = Post.objects.filter(category__route = 'maps')

  request.session['map_urls'] = {md5(str(m.pk).encode()).hexdigest(): m.pk for m in maps}

user_logged_in.connect(do_stuff)
#end TODO

def post_list(request, tags=None, category=None, author=None):

  t = c = None
  if category:
    c = get_object_or_404(Category, route=category)

  if tags:
    t = tags.split(",")

  query = {
    'is_public': True,
    'tags__name__in': t,
    'author__username': author,
    'category': c,
  }

  q = {k: v for k, v in query.items() if v is not None}

  posts = Post.objects.filter(**q).distinct().order_by('-created_date', 'title')

  return render(request, 'cms/post_list.html', {
    'posts': posts,
    'category': c,
    'tags': tags,
    'taglist': t,
    'author': author
  })

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'cms/post_detail.html', {'post': post})

def post_new(request,category):
  categoryObj = get_object_or_404(Category, route=category)

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
      form.save_m2m()
      return redirect('post_detail', pk=post.pk)
  else:
    form = formClass()

  return render(request, 'cms/post_edit.html', {'form': form, 'category':  categoryObj, 'is_post_add': True})

def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)

  if post.category.kind == '0':
    formClass = BinaryPostForm
  elif post.category.kind == '1':
    formClass = TextPostForm
  else:
    formClass = PostForm

  if request.method == "POST":
    form = formClass(request.POST, request.FILES, instance=post)

    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()

      post.save()
      form.save_m2m()
      return redirect('post_detail', pk=post.pk)
  else:
    form = formClass(instance=post)

  return render(request, 'cms/post_edit.html', {'form': form, 'category': post.category, 'is_post_edit': True})

def post_delete(request, pk):
  post = get_object_or_404(Post, pk=pk)
  category = post.category.route
  post.delete()
  return redirect('category_list', category=category)

def comment_new(request, pk):
  post = get_object_or_404(Post, pk=pk)

  if request.method == "POST":
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.author = request.user
      comment.post = post
      comment.save()

      return get_comment_url(post.pk, comment.pk)

  return redirect('post_detail', pk=post.pk)

def comment_edit(request, pk, cpk):
  post = get_object_or_404(Post, pk=pk)
  edited_comment = get_object_or_404(Comment, pk=cpk)

  if request.method == "POST":
    form = CommentForm(request.POST, instance=edited_comment)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.author = request.user
      comment.post = post
      comment.modifed_date = timezone.now()
      comment.save()

      return get_comment_url(post.pk, comment.pk)
  else:
    form = CommentForm(instance=edited_comment)

  return render(request, 'cms/comment_edit.html', {'form': form})

def comment_reply(request, pk, cpk):
  post = get_object_or_404(Post, pk=pk)
  parent = get_object_or_404(Comment, pk=cpk)

  if request.method == "POST":
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.author = request.user
      comment.post = post
      comment.parent = parent
      comment.save()

      return get_comment_url(post.pk, comment.pk)
  else:
    form = CommentForm()

  return render(request, 'cms/comment_edit.html', {'form': form, 'parent': parent})

def comment_delete(request, pk, cpk):
  post = get_object_or_404(Post, pk=pk)
  comment = get_object_or_404(Comment, pk=cpk)

  comment.is_deleted = True
  comment.save()

  return redirect('post_detail', pk=post.pk)

def get_comment_url(pk, cpk):
  return HttpResponseRedirect('%s#comment%s' % (reverse('post_detail', kwargs={'pk':pk}), cpk))

def serve_map_file(request, map_hash):
  try:
    map_pk = request.session['map_urls'][map_hash]
    m = get_object_or_404(Post, pk=map_pk)

    # import sys
    # for key, value in request.session.items(): print('{} => {}'.format(key, value), file=sys.stderr)

    return HttpResponse(m.file.file, content_type='image/jpg')
  except KeyError:
    raise Http404("No map found.")
