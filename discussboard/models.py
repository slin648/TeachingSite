from django.db import models
from django.contrib.auth.models import User
from siteindex.models import Lesson
from django.urls import reverse

# Create your models here.


class Board(models.Model):
    """用于表示一个课程的讨论板的模型"""
    lesson = models.OneToOneField(
        Lesson, blank=True, null=True, related_name='board', on_delete=models.CASCADE)

    description = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('board-topics', args=[str(self.id)])

    def __str__(self):
        return f"{self.lesson}"


class Topic(models.Model):
    """用于表示主题帖的模型"""
    subject = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(
        Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(
        User, related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.board}-{self.subject}"


class Post(models.Model):
    """用于表示一个回帖的模型"""
    message = models.TextField(max_length=5000)
    topic = models.ForeignKey(
        Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.topic}-{self.created_by}"
