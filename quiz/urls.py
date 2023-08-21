from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.QuizListView.as_view(), name='quiz-list-view'),
    path('quizzes/<uuid:pk>', views.QuizDetailView.as_view(), name='quiz-view'),
    path('quizzes/<uuid:pk>/data/', views.quiz_data_view, name='quiz-data-view'),
    path('quizzes/<uuid:pk>/save/', views.save_quiz_view, name='save-view'),
]

urlpatterns += [
    path('myresults/', views.MyResultsListView.as_view(), name='my-results'),
]
