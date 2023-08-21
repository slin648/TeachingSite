from siteindex.models import Lesson, Record
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Answer, Quiz, Question, Result

from django.http import JsonResponse

# Create your views here.


class QuizListView(LoginRequiredMixin, ListView):
    """
    测验列表视图
    """
    model = Quiz


class QuizDetailView(LoginRequiredMixin, DetailView):
    """
    测验详细信息视图
    """
    model = Quiz


def quiz_data_view(request, pk):
    """
    测验内容视图
    """
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})

    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, pk):
    """
    测验保存提交视图
    """
    if request.is_ajax():

        questions = []

        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        # 计分
        score = 0
        # 获取该测验问题数量
        question_num = quiz.get_question_num()
        multiplier = 100/question_num

        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            # 选了一个选项
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    # 选对了
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    # 没有选对
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append(
                    {str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            # 没选
            else:
                results.append({str(q): 'not_answered'})

        # 最后分数四舍五入到两位小数
        score_ = round(score*multiplier, 2)

        if score_ >= quiz.required_score_to_pass:
            pass_status = 't'
            Result.objects.create(quiz=quiz, user=user,
                                  score=score_, pass_or_not=pass_status)

            try:
                record = Record.objects.get(user=user)
            except:
                Record.objects.create(user=user)
                record = Record.objects.get(user=user)

                lesson = Lesson.objects.get(quiz=quiz)
                record.lesson_finished.add(lesson)
                record.save()

            else:
                lesson = Lesson.objects.get(quiz=quiz)
                record.lesson_finished.add(lesson)
                record.save()

            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            pass_status = 'f'
            Result.objects.create(quiz=quiz, user=user,
                                  score=score_, pass_or_not=pass_status)

            return JsonResponse({'passed': False, 'score': score_, 'results': results})


class MyResultsListView(LoginRequiredMixin, ListView):
    """
    成绩视图
    """
    model = Result

    def get_queryset(self):
        return Result.objects.filter(user=self.request.user)
