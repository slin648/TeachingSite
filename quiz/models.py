from siteindex.models import Lesson
from django.contrib.auth.models import User
from django.db import models
import uuid
import siteindex

# Create your models here.


class Quiz(models.Model):
    """用于表示测验的模型"""
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text='该测验的唯一ID')

    lesson = models.OneToOneField(
        Lesson, blank=True, null=True, related_name='quiz', on_delete=models.CASCADE)

    time = models.IntegerField(help_text="该测验预计完成的分钟数")

    required_score_to_pass = models.IntegerField(
        help_text="通过分数(百分制)")

    def __str__(self):
        return f"{self.lesson}"

    def get_questions(self):
        return self.question_set.all()

    def get_question_num(self):
        return len(self.question_set.all())

    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    """用于表示测验中的单个问题的模型"""
    text = models.CharField(max_length=500)
    quiz = models.ManyToManyField(Quiz)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    """用于表示测验问题的答案的模型"""
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question.text}-{self.text}-{self.correct}"


class Result(models.Model):
    """用于表示测验结果的模型"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    STATUS_list = (
        ('t', '通过'),
        ('f', '未通过'),
    )

    pass_or_not = models.CharField(
        max_length=1,
        choices=STATUS_list,
        blank=True,
        default='f',
    )

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f'{self.quiz}-{self.user}-{self.pk}'
