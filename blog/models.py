from django.db import models
from django.utils import timezone
from django.urls import reverse
from martor.models import MartorField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = MartorField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_message_as_markdown(self):
        return self.content
