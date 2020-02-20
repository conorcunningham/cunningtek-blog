from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from . models import Post


class PostAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminMartorWidget},
    # }
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post)
