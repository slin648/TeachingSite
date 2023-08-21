from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lessons/', views.LessonListView.as_view(), name='lessons'),
    path('lesson/<int:pk>', views.LessonDetailView.as_view(), name='lesson-detail'),
]

urlpatterns += [
    path('lecturers/', views.LecturerListView.as_view(), name='lecturers'),
    path('lecturer/<int:pk>', views.LecturerDetailView.as_view(),
         name='lecturer-detail'),
]

urlpatterns += [
    path('register', views.Register, name='register'),
]
