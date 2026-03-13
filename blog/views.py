"""
Views for the blog app — Post list, detail, category, and tag filtering.
"""

from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


class PostListView(ListView):
    """List all published blog posts with pagination."""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(published=True).select_related('category', 'author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['recent_posts'] = Post.objects.filter(published=True)[:5]
        return context


class PostDetailView(DetailView):
    """Single blog post detail page."""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(published=True).select_related('category', 'author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.filter(published=True).exclude(pk=self.object.pk)[:5]
        return context


class CategoryPostListView(ListView):
    """Posts filtered by category."""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            published=True, category__slug=self.kwargs['slug']
        ).select_related('category', 'author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class TagPostListView(ListView):
    """Posts filtered by tag."""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            published=True, tags__slug=self.kwargs['slug']
        ).select_related('category', 'author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_tag'] = Tag.objects.get(slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context
