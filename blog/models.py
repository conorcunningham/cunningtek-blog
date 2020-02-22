from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from martor.models import MartorField
from django.utils.html import mark_safe
from markdown import markdown
import bleach

ALLOWED_TAGS = [
    'a',
    'abbr',
    'acronym',
    'b',
    'blockquote',
    'br',
    'code',
    'em',
    'i',
    'li',
    'ol',
    'strong',
    'ul',
    'p',
    'table',
    'tbody',
    'thead',
    'tr',
    'td',
    'th',
    'div',
    'span',
    'hr',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'pre',
    'int:pk',
    'module'
    '>'
    # Update doc/user/markdown.rst if you change this!
]

ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'class'],
    'abbr': ['title'],
    'acronym': ['title'],
    'table': ['width'],
    'td': ['width', 'align'],
    'div': ['class'],
    'p': ['class'],
    'span': ['class', 'title'],
}

ALLOWED_PROTOCOLS = ['http', 'https', 'mailto', 'tel']


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f"Title: {self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_message_as_markdown(self):
        return self.content
        # return bleach.clean(
        #     self.content,
        #     tags=ALLOWED_TAGS,
        #     attributes=ALLOWED_ATTRIBUTES,
        #     protocols=ALLOWED_PROTOCOLS,
        # )


class ViewingRecord(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    source = models.GenericIPAddressField()

