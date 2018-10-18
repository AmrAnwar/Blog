# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse
from colorfield.fields import ColorField
from markdown_deux import markdown
from django.utils.safestring import mark_safe
User = get_user_model()

types = (
    ('a', 'programming'),
    ('b', 'personal'),
    ('c', 'Brain storming'),

)


def upload_location(instance, filename):
    if instance.id:
        new_id = instance.id
    else:
        new_id = Post.objects.order_by("id").last().id + 1
    return "%s/%s" % (new_id, filename)


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, default=1, null=False)
    title = models.CharField(null=False, max_length=50)
    content = models.TextField(null=False, blank=False)
    # content = MarkdownField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(unique=True)
    wait = models.BooleanField(default=False)
    color = ColorField(default='#FFFFFF')
    type = models.CharField(choices=types, max_length=3, default=1)
    image = models.ImageField(
        upload_to=upload_location,
        null=False, blank=False,
        height_field='height_field',
        width_field='width_field',

    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    class Meta:
        ordering = ["-timestamp"]

    def __unicode__(self):
        return "%s:%s" % (self.user, self.title)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={'slug': self.slug})

    def get_markdown(self):
        content = self.content
        return mark_safe(markdown(content))


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
