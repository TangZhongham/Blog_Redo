from django.contrib import admin
from .models import Category, Tag, Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_time', 'modified_time', 'excerpt', 'author')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)