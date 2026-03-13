"""
Models for the core app — Projects, Experience, ContactMessage.
"""

from django.db import models


class Experience(models.Model):
    """Work experience entry for the timeline."""
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50, help_text="e.g. February 2025")
    end_date = models.CharField(max_length=50, default="Present")
    description = models.TextField(
        help_text="Use bullet points separated by newlines for multiple items."
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first).")

    class Meta:
        ordering = ['order', '-pk']
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.role} at {self.company}"

    def description_lines(self):
        """Return description split into individual bullet points."""
        return [line.strip('- ').strip() for line in self.description.strip().split('\n') if line.strip()]


class Project(models.Model):
    """Portfolio project entry."""
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    tech_stack = models.CharField(
        max_length=500,
        help_text="Comma-separated list of technologies."
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='intermediate')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    demo_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created']

    def __str__(self):
        return self.title

    def tech_list(self):
        """Return tech stack as a list."""
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class ContactMessage(models.Model):
    """Contact form submission."""
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
