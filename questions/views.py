from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from django.contrib.auth.models import User

from django.utils import timezone

from django.urls import reverse

from .models import Question, Comment

import datetime

def index(request):
    return render(request, 'questions/list.html')

def questionslist(request):
    question_list = Question.objects.order_by('-pub_date')[:2]
    return render(request, 'questions/list.html', {'question_list': question_list})

def question(request, question_id):
    try:
        a = Question.objects.get( id = question_id )
    except:
        raise Http404("Вопрос не найден!")

    comments_list = a.comment_set.order_by('id')
    
    return render(request, 'questions/question.html', {'question': a, 'comments_list': comments_list})

def leave_comment(request, question_id, user_id):
    try:
        a = Question.objects.get( id = question_id )
        b = User.objects.get(id = user_id)
    except:
        raise Http404("Вопрос не найден!")


    a.comment_set.create(author_name = b, comment_text = request.POST['text'], pub_date = datetime.datetime.now())
    
    return HttpResponseRedirect( reverse('PageWithQuestion', args = (a.id,)) )

def page_for_new_question(request):
    return render(request, 'questions/pagefornewquestion.html')


def new_question(request, user_id):
    try:
        b = User.objects.get(id = user_id)
    except:
        raise Http404("Страница не найдена!")

    New_Question = Question(author_name = b, question_theme = request.POST['themequestion'], question_text = request.POST['textquestion'], pub_date = datetime.datetime.now())
    New_Question.save()

    My_question = Question.objects.get(question_text = request.POST['textquestion'])
    comments_list = My_question.comment_set.order_by('id')
    
    return render(request, 'questions/question.html', {'question': My_question, 'comments_list': comments_list})

def delete_the_question(request, question_id):
    try:
        a = Question.objects.get( id = question_id )
        a.delete()
    except:
        raise Http404("Вопрос не найден!")
    
    question_list = Question.objects.order_by('-pub_date')
    return render(request, 'questions/list.html', {'question_list': question_list})

def delete_the_comment(request, comment_id, question_id):
    try:
        a = Question.objects.get( id = question_id )
        b = Comment.objects.get( id = comment_id )
        b.delete()
    except:
        raise Http404("Комментарий не найден!")
    
    
    
    comments_list = a.comment_set.order_by('id')
    
    return render(request, 'questions/question.html', {'question': a, 'comments_list': comments_list})

def statusOfQuestion(request, question_id):
    try:
        a = Question.objects.get( id = question_id )
        if a.status == False:
            a.status = True
        else:
            a.status = False
        a.save()
    except:
        raise Http404("Вопрос не найден!")
    
    comments_list = a.comment_set.order_by('pub_date')
    return render(request, 'questions/question.html', {'question': a, 'comments_list': comments_list})

def statusOfComment(request, comment_id, question_id):
    try:
        a = Comment.objects.get( id = comment_id )
        b = Question.objects.get( id = question_id )
        if a.status == False:
            a.status = True
        else:
            a.status = False
        a.save()
    except:
        raise Http404("Комментарий не найден!")
    
    comments_list = b.comment_set.order_by('pub_date')
    return HttpResponseRedirect( reverse('PageWithQuestion', args = (b.id,)) )