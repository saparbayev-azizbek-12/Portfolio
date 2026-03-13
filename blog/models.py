"""
Models for the blog app — Category, Tag, Post.
"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import markdown


class Category(models.Model):
    """Blog post category."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})


class Tag(models.Model):
    """Blog post tag."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'slug': self.slug})


class Post(models.Model):
    """Blog post with markdown content support."""
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField(help_text="Write content in Markdown format.")
    excerpt = models.TextField(max_length=500, blank=True, help_text="Short summary for list views.")
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # SEO fields
    meta_title = models.CharField(max_length=160, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['-pub_date', '-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def content_html(self):
        """Convert markdown content to HTML."""
        return markdown.markdown(
            self.content,
            extensions=['fenced_code', 'codehilite', 'tables', 'toc']
        )

    def reading_time(self):
        """Estimate reading time in minutes."""
        word_count = len(self.content.split())
        minutes = max(1, round(word_count / 200))
        return minutes
