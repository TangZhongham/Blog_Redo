from django.contrib import admin
from .models import Category, Tag, Post, UserPost

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'created_time', 'modified_time', 'author')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(UserPost)