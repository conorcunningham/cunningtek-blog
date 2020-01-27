from django.db import models
from django.utils import timezone
from django.urls import reverse
from martor.models import MartorField
from django.utils.html import mark_safe
from markdown import markdown
import bleach


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_message_as_markdown(self):
        return bleach.clean(self.content)
        #return mark_safe(markdown(self.content, safe_mode='escape'))
