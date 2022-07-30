import datetime
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Question(models.Model):
    author_name = models.ForeignKey(User, on_delete = models.CASCADE)
    question_theme = models.CharField('Тема вопроса', max_length = 200)
    question_text = models.TextField('Содержание вопроса', max_length = 500)
    pub_date = models.DateTimeField('Дата публикации')
    status = models.BooleanField(default = False)
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question_theme

    def check_bublic_time(self):
        return self.pubdate >= (timezone.now() - datetime.timedelta(days = 1))

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author_name = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.CharField('Содежрание комментария', max_length = 500)
    pub_date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.author_name

    def check_bublic_time(self):
        return self.pubdate >= (timezone.now() - datetime.timedelta(days = 1))