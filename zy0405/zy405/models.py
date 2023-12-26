from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    categoryName = models.CharField('分类', max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.categoryName


class Tags(models.Model):
    tagsName = models.CharField('标签', max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.tagsName


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    intro = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name='标签')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
