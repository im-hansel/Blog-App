from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', "Draft"
        PUBLISHED = 'PB', "Published"

    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
