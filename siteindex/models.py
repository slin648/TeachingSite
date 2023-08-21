from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from django.db import models

# Create your models here.


class Syllabus(models.Model):
    """用于表示课程大纲的模型"""

    STATUS_list = (
        ('a', '当前应用'),
        ('b', '候补1'),
        ('c', '候补2'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_list,
        blank=True,
        default='a',
        unique=True,
    )

    intro = models.TextField(max_length=10000, null=True,
                             blank=True, help_text='课程大纲介绍')

    image = models.ImageField(upload_to='syllabus', blank=True, null=True)

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/media/default.png'

    def __str__(self):
        return self.status


class Lecturer(models.Model):
    """用于表示课程讲师的模型"""
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    intro = models.TextField(max_length=10000, null=True,
                             blank=True, help_text='讲师简介')

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    user = models.OneToOneField(
        User, blank=True, null=True, related_name='lecturer', on_delete=models.CASCADE)

    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return '/media/defaultavatar.png'

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('lecturer-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.title}, {self.name}'


class Lesson(models.Model):
    """用于表示一节课程的模型"""
    title = models.CharField(max_length=200)
    lecturer = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='输入该节课程的简介')
    date_of_release = models.DateField(null=True, blank=True)

    precondition = models.OneToOneField(
        "Lesson", blank=True, null=True, related_name='precond_of', on_delete=models.CASCADE)

    video = models.FileField(upload_to='videos', blank=True, null=True)

    image_1 = models.ImageField(upload_to='images', blank=True, null=True)
    parag_1 = models.TextField(max_length=100000, help_text='正文第一段', null=True)

    image_2 = models.ImageField(upload_to='images', blank=True, null=True)
    parag_2 = models.TextField(
        max_length=100000, help_text='正文第二段', null=True, blank=True)

    image_3 = models.ImageField(upload_to='images', blank=True, null=True)
    parag_3 = models.TextField(
        max_length=100000, help_text='正文第三段', null=True, blank=True)

    def video_url(self):
        if self.video and hasattr(self.video, 'url'):
            return self.video.url
        else:
            return '/media/default.mp4'

    def image_1_url(self):
        if self.image_1 and hasattr(self.image_1, 'url'):
            return self.image_1.url
        else:
            return '/media/default.png'

    def image_2_url(self):
        if self.image_2 and hasattr(self.image_2, 'url'):
            return self.image_2.url
        else:
            return '/media/default.png'

    def image_3_url(self):
        if self.image_3 and hasattr(self.image_3, 'url'):
            return self.image_3.url
        else:
            return '/media/default.png'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', args=[str(self.id)])


class Record(models.Model):
    """用于表示每个用户当前学习情况的模型"""
    user = models.OneToOneField(
        User, related_name='record', on_delete=models.CASCADE)

    lesson_finished = models.ManyToManyField(
        Lesson, related_name='finished', blank=True)

    def __str__(self):
        return f'{self.user}'
