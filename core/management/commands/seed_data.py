"""
Management command to seed the database with initial portfolio data.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Experience, Project
from blog.models import Category, Tag, Post


class Command(BaseCommand):
    help = 'Seed database with initial portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created superuser: admin / admin123'))
        else:
            user = User.objects.get(username='admin')

        # Experiences
        Experience.objects.all().delete()
        Experience.objects.create(
            company='AmuSoft',
            role='Backend Developer (Django)',
            start_date='February 2025',
            end_date='Present',
            description='Developing scalable web applications using Django and REST APIs\nDatabase optimization and performance tuning\nIntegrating AI/ML models into production systems',
            order=1,
        )
        Experience.objects.create(
            company='MAAB Innovation',
            role='Database Programmer',
            start_date='October 2025',
            end_date='Present',
            description='Designing and managing complex databases (PostgreSQL, MySQL)\nWriting efficient SQL queries and stored procedures\nCollaborating on data-driven business solutions',
            order=2,
        )
        self.stdout.write(self.style.SUCCESS('Created 2 experiences'))

        # Projects
        Project.objects.all().delete()
        Project.objects.create(
            title='Warehouse',
            slug='warehouse',
            description='Warehouse automation web app for tracking incoming/outgoing goods, inventory management, and income/expense reporting. Features real-time dashboard with analytics.',
            tech_stack='Django, MySQL, HTML/CSS, JavaScript',
            level='intermediate',
            demo_url='https://warehousedemo.pythonanywhere.com',
            featured=True,
            order=1,
        )
        Project.objects.create(
            title='LMS',
            slug='lms',
            description='Distance learning platform for university students featuring assignments submission, automated grading, progress tracking, and interactive course materials.',
            tech_stack='Django, PostgreSQL, JavaScript, Tailwind CSS',
            level='advanced',
            featured=True,
            order=2,
        )
        Project.objects.create(
            title='ML-Zone',
            slug='ml-zone',
            description='Collection of interactive machine learning projects including digit recognition, house price prediction, and text classification with live demos.',
            tech_stack='Python, Scikit-learn, NumPy, Pandas, Django',
            level='intermediate',
            demo_url='https://mlzone.pythonanywhere.com/',
            featured=True,
            order=3,
        )
        self.stdout.write(self.style.SUCCESS('Created 3 projects'))

        # Blog Categories & Tags
        Category.objects.all().delete()
        Tag.objects.all().delete()
        cat_django = Category.objects.create(name='Django', slug='django')
        cat_ai = Category.objects.create(name='AI & ML', slug='ai-ml')
        cat_tips = Category.objects.create(name='Dev Tips', slug='dev-tips')

        tag_python = Tag.objects.create(name='Python', slug='python')
        tag_web = Tag.objects.create(name='Web Dev', slug='web-dev')
        tag_ml = Tag.objects.create(name='Machine Learning', slug='machine-learning')
        tag_django = Tag.objects.create(name='Django', slug='django')

        # Blog Posts
        Post.objects.all().delete()
        p1 = Post.objects.create(
            title='Getting Started with Django REST Framework',
            slug='getting-started-django-rest-framework',
            author=user,
            content='## Introduction\n\nDjango REST Framework (DRF) is a powerful toolkit for building Web APIs in Django.\n\n## Why DRF?\n\n- **Serialization** that supports ORM and non-ORM data sources\n- **Authentication** policies including OAuth1a and OAuth2\n- **Browsable API** — huge usability win for developers\n\n## Quick Setup\n\n```python\npip install djangorestframework\n```\n\nAdd to your `INSTALLED_APPS`:\n\n```python\nINSTALLED_APPS = [\n    ...\n    \'rest_framework\',\n]\n```\n\n## Creating Your First Serializer\n\n```python\nfrom rest_framework import serializers\nfrom .models import Article\n\nclass ArticleSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = Article\n        fields = [\'id\', \'title\', \'content\', \'created\']\n```\n\nDRF makes it incredibly easy to build robust APIs. Stay tuned for more advanced topics!',
            excerpt='Learn how to set up Django REST Framework and create your first API endpoint with serializers and views.',
            category=cat_django,
            published=True,
            pub_date=timezone.now(),
        )
        p1.tags.add(tag_python, tag_django, tag_web)

        p2 = Post.objects.create(
            title='Introduction to Machine Learning with Scikit-learn',
            slug='intro-machine-learning-scikit-learn',
            author=user,
            content='## What is Machine Learning?\n\nMachine Learning is a subset of AI that enables systems to learn from data.\n\n## Getting Started\n\n```python\nfrom sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\n\n# Load data\niris = load_iris()\nX_train, X_test, y_train, y_test = train_test_split(\n    iris.data, iris.target, test_size=0.2\n)\n\n# Train model\nclf = RandomForestClassifier(n_estimators=100)\nclf.fit(X_train, y_train)\n\n# Evaluate\nprint(f"Accuracy: {clf.score(X_test, y_test):.2f}")\n```\n\n## Key Concepts\n\n1. **Supervised Learning** — labeled training data\n2. **Unsupervised Learning** — finding patterns in unlabeled data\n3. **Reinforcement Learning** — learning through rewards\n\nMachine learning is transforming every industry. Start your journey today!',
            excerpt='A beginner-friendly introduction to machine learning concepts and hands-on coding with Scikit-learn.',
            category=cat_ai,
            published=True,
            pub_date=timezone.now() - timezone.timedelta(days=3),
        )
        p2.tags.add(tag_python, tag_ml)

        self.stdout.write(self.style.SUCCESS('Created blog posts'))
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
