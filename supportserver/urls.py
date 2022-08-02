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
    path('questionslist/<int:question_id>/newoldquestionpage/newoldquestion', views.newoldquestion, name='newoldquestion'),
    path('questionslist/<int:question_id>/newoldquestionpage/', views.newoldquestionpage, name='newoldquestionpage'),
    path('questionslist/<int:comment_id>-<int:question_id>/newoldcommentpage/newoldcomment', views.newoldcomment, name='newoldcomment'),
    path('questionslist/<int:comment_id>-<int:question_id>/newoldcommentpage/', views.newoldcommentpage, name='newoldcommentpage'),
    path('questionslist/<int:comment_id>-<int:question_id>/newmarkpage/newmark', views.newmark, name='newmark'),
    path('questionslist/<int:comment_id>-<int:question_id>/newmarkpage', views.newmarkpage, name='newmarkpage'),
    path('questionslist/<int:comment_id>-<int:question_id>/deletecomment', views.delete_the_comment, name='deletecomment'),
    path('questionslist/<int:comment_id>-<int:question_id>/statusOfComment', views.statusOfComment, name='statusOfComment'),
    path('questionslist/<int:question_id>/statusOfQuestion', views.statusOfQuestion, name='statusOfQuestion'),
    path('questionslist/<int:question_id>/', views.question, name='PageWithQuestion'),
    re_path(r'^questionslist', views.questionslist, name='PageWithQuestions'),
    path('admin/', admin.site.urls),
    path('', views.questionslist, name='StartPage'),
]
