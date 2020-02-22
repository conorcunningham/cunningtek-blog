from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from . models import Post, ViewingRecord


class PostAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminMartorWidget},
    # }
    prepopulated_fields = {'slug': ('title',)}


class ViewingRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "source"]


admin.site.register(Post)
admin.site.register(ViewingRecord)
