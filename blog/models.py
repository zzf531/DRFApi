from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100) # 标题
    body = models.TextField()  # 文章主体
    created_time = models.DateTimeField(auto_now=True)  # 创建时间
    modified_time = models.DateTimeField(auto_now_add=True)  # 修改时间
    excerpt = models.CharField(max_length=200, default='')  # 文章的摘要
    owner = models.ForeignKey('auth.User', related_name='snippetss', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

