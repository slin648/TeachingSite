from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.http import JsonResponse

# Create your views here.
from .models import Syllabus, Lecturer, Lesson, Record


def index(request):
    """
    主页视图
    """
    lesson_num = Lesson.objects.all().count()
    lecturer_num = Lecturer.objects.all().count()

    return render(
        request,
        'index.html',
        context={'lesson_num': lesson_num, 'lecturer_num': lecturer_num},
    )


class LecturerListView(LoginRequiredMixin, generic.ListView):
    model = Lecturer
    paginate_by = 20


class LecturerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Lecturer


class LessonListView(LoginRequiredMixin, generic.ListView):
    """
    课程列表视图
    """
    model = Lesson
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(LessonListView, self).get_context_data(**kwargs)
        context.update({
            'syllabus': Syllabus.objects.get(status='a'),
        })
        return context


class LessonDetailView(LoginRequiredMixin, generic.DetailView):
    model = Lesson


def Register(request):
    """
    用户注册视图
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
