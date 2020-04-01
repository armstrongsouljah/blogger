from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from .utils import generate_unique_slug


User = get_user_model()


class Blog(models.Model):
    name = models.CharField(max_length=234)
    slug = models.CharField(max_length=255, blank=True)
    tagline = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class Entry(models.Model):
    headline = models.CharField(max_length=234)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    authors = models.ManyToManyField(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.headline}"
    
    class Meta:
        ordering = ['-pub_date']


def post_save_receiver(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance, 6)


post_save.connect(post_save_receiver, Blog)

