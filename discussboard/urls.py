from django.urls import path
from . import views

urlpatterns = [
    path('boards', views.home, name='board-home-view'),

    path('board/<int:pk>', views.board_topics, name='board-topics'),
    path('board/<int:pk>/new', views.new_topic, name='new-topic'),
    path('board/<int:pk>/topic/<int:topic_pk>',
         views.topic_posts, name='topic-posts'),
    path('board/<int:pk>/topic/<int:topic_pk>/reply',
         views.reply_topic, name='reply-topic'),
]
