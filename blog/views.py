from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm

def post_list(request):
    template_name = 'blog/post_list.html'
    data = Post.objects.all()
    return render(request, template_name, {'data': data})

def post_detail(request, pk):
    template_name = 'blog/post_detail.html'
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, template_name, {'post': post})

def post_new(request):
    template_name = 'blog/post_edit.html'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, template_name, {'form': form})