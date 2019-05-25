from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from . models import Post


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Post)
