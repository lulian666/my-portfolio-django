from django.db import models
import uuid

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.body[:50]


class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    logo = models.ImageField(null=True, default="skill.png")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Endorsement(models.Model):
    name = models.CharField(max_length=200, null=True)
    body = models.TextField()
    featured = models.BooleanField(default=False, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:50]


class Question(models.Model):

    TYPES = (
        ('backend', 'backend'),
        ('frontend', 'frontend'),
        ('fullstack', 'fullstack'),
    )

    answer = models.CharField(max_length=200, choices=TYPES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.answer
