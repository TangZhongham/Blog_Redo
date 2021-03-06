from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 标题
    title = models.CharField(max_length=70)

    # 正文
    body = RichTextUploadingField(config_name='default')

    # 时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # excerpt
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=True)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=True)

    image = models.ImageField(upload_to='upload/carousel/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


# user
class UserPost(models.Model):
    # 标题
    title = models.CharField(max_length=70)

    # 正文
    body = RichTextUploadingField(config_name='default')

    # 时间
    created_time = models.DateField(auto_now_add=True)

    # excerpt
    # excerpt = models.CharField(max_length=200, blank=True)

    author = models.ForeignKey(User, on_delete=True)

    # image = models.ImageField(upload_to='upload/user/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})