from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import NewTopicForm, PostForm
from .models import Board, Topic, Post

# Create your views here.


def home(request):
    """
    讨论板列表视图
    """
    boards = Board.objects.all()
    return render(request, 'discussboard/home.html', {'boards': boards})


def board_topics(request, pk):
    """
    主题帖列表视图
    """
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'discussboard/topics.html', {'board': board})


@login_required
def new_topic(request, pk):
    """
    新建主题帖视图
    """
    board = get_object_or_404(Board, pk=pk)
    # 新建一个主题帖，内容作为主题帖的第一个帖子
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )

            return redirect('board-topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'discussboard/new_topic.html', {'board': board, 'form': form})


@login_required
def topic_posts(request, pk, topic_pk):
    """
    主题帖详情视图
    """
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'discussboard/topic_posts.html', {'topic': topic})


@login_required
def reply_topic(request, pk, topic_pk):
    """
    回帖视图
    """
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic-posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'discussboard/reply_topic.html', {'topic': topic, 'form': form})
