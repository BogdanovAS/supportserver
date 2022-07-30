from django.contrib import admin
from django.urls import path, re_path, include
from questions import views

urlpatterns = [
    re_path(r'^accounts', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('questionslist/new_question-<int:user_id>', views.new_question, name='new_question'),
    path('questionslist/new_question', views.page_for_new_question, name='page_for_new_question'),
    path('questionslist/<int:question_id>-<int:user_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('questionslist/<int:question_id>/deletequestion', views.delete_the_question, name='deletequestion'),
    path('questionslist/<int:comment_id>-<int:question_id>/deletecomment', views.delete_the_comment, name='deletecomment'),
    path('questionslist/<int:question_id>/', views.question, name='PageWithQuestion'),
    re_path(r'^questionslist', views.questionslist, name='PageWithQuestions'),
    path('admin/', admin.site.urls),
    path('', views.index, name='StartPage'),
]
