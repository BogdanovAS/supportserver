from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from django.core.exceptions import PermissionDenied


from django.contrib.auth.models import User

from django.utils import timezone

from django.urls import reverse

from .models import Question, Comment

import datetime


def questionslist(request):                 #отображение списка вопросов
    question_list = Question.objects.order_by('-pub_date')
    return render(request, 'questions/list.html', {'question_list': question_list})

def question(request, question_id):                 #отображение вопроса
    try:
        a = Question.objects.get( id = question_id )
    except:
        raise Http404("Вопрос не найден!")

    comments_list = a.comment_set.order_by('id')
    
    return render(request, 'questions/question.html', {'question': a, 'comments_list': comments_list})

def leave_comment(request, question_id, user_id):                 #оставить комментарий
    try:
        a = Question.objects.get( id = question_id )
        b = User.objects.get(id = user_id)
    except:
        raise Http404("Вопрос не найден!")


    a.comment_set.create(author_name = b, comment_text = request.POST['text'], pub_date = datetime.datetime.now())
    
    return HttpResponseRedirect( reverse('PageWithQuestion', args = (a.id,)) )

def page_for_new_question(request):                 #форма для нового вопроса
    return render(request, 'questions/pagefornewquestion.html')


def new_question(request, user_id):                 #задать новый вопрос
    try:
        b = User.objects.get(id = user_id)
    except:
        raise Http404("Страница не найдена!")

    New_Question = Question(author_name = b, question_theme = request.POST['themequestion'], question_text = request.POST['textquestion'], pub_date = datetime.datetime.now())
    New_Question.save()

    My_question = Question.objects.get(question_text = request.POST['textquestion'])
    comments_list = My_question.comment_set.order_by('id')
    
    return render(request, 'questions/question.html', {'question': My_question, 'comments_list': comments_list})

def delete_the_question(request, question_id):                 #удалить вопрос
    try:
        a = Question.objects.get( id = question_id )
        a.delete()
    except:
        raise Http404("Вопрос не найден!")
    
    question_list = Question.objects.order_by('-pub_date')
    return render(request, 'questions/list.html', {'question_list': question_list})

def delete_the_comment(request, comment_id, question_id):                 #удалить комментарий
    try:
        a = Question.objects.get( id = question_id )
        b = Comment.objects.get( id = comment_id )
        b.delete()
    except:
        raise Http404("Комментарий не найден!")
    
    
    
    comments_list = a.comment_set.order_by('id')
    
    return render(request, 'questions/question.html', {'question': a, 'comments_list': comments_list})

def statusOfQuestion(request, question_id):                 #метка для вопроса(получен верный ответ или нет)
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

def statusOfComment(request, comment_id, question_id):                 #метка для ответа(является ответ верным или нет)
    try:
        a = Comment.objects.get( id = comment_id )
        b = Question.objects.get( id = question_id )
        if a.status == False:
            a.status = True
            b.status = True
            b.save()
        else:
            a.status = False
        a.save()
    except:
        raise Http404("Комментарий не найден!")
    
    comments_list = b.comment_set.order_by('pub_date')
    return HttpResponseRedirect( reverse('PageWithQuestion', args = (b.id,)) )

def newmarkpage(request, comment_id, question_id):                 #форма для оценки ответа(рейтинг)
    try:
        a = Comment.objects.get( id = comment_id )
        b = Question.objects.get( id = question_id )
    except:
        raise Http404("Комментарий не найден!")
    return render(request, 'questions/newmarkpage.html', {'question': b, 'comment': a})

def newmark(request, comment_id, question_id):                 #оценка ответа(рейтинг)
    try:
        a = Comment.objects.get( id = comment_id )
        b = Question.objects.get( id = question_id )
    except:
        raise PermissionDenied()
    
    if len(request.POST['mark']) != 1 or int(request.POST['mark']) < 1 or int(request.POST['mark']) > 5:
        raise PermissionDenied()

    if a.marks == False:
        a.rating = request.POST['mark']
        a.marks = True
    else:
        a.rating = round((a.rating + int(request.POST['mark']))/2, 1)
    
    a.save()

    comments_list = b.comment_set.order_by('pub_date')
    return HttpResponseRedirect( reverse('PageWithQuestion', args = (b.id,)) )

def newoldcommentpage(request, comment_id, question_id):                 #страница для редактирования комментария
    try:
        a = Comment.objects.get( id = comment_id )
        b = Question.objects.get( id = question_id )
    except:
        raise Http404("Комментарий не найден!")
    return render(request, 'questions/newoldcomment.html', {'question': b, 'comment': a})

def newoldcomment(request, comment_id, question_id):                 #редактирование комментария
    try:
        a = Comment.objects.get( id = comment_id )
        b = Question.objects.get( id = question_id )

    except:
        raise Http404("Комментарий не найден!")


    a.comment_text = request.POST['textcomment']
    a.save()
    
    comments_list = b.comment_set.order_by('pub_date')
    return render(request, 'questions/question.html', {'question': b, 'comments_list': comments_list})

def newoldquestionpage(request, question_id):                 #страница для редактирования вопроса
    try:
        b = Question.objects.get( id = question_id )
    except:
        raise Http404("Вопрос не найден!")
    return render(request, 'questions/newoldquestion.html', {'question': b})

def newoldquestion(request, question_id):                 #редактирование вопроса
    try:
        b = Question.objects.get( id = question_id )

    except:
        raise Http404("Вопрос не найден!")


    b.question_text = request.POST['textquestion']
    b.save()
    
    comments_list = b.comment_set.order_by('pub_date')
    return render(request, 'questions/question.html', {'question': b, 'comments_list': comments_list})