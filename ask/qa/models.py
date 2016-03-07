# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# вопрос
class Question(models.Model):
    # заголовок вопроса
    title = models.CharField(max_length=255)
    # полный текст вопроса
    text = models.TextField()
    # дата добавления вопроса
    added_at = models.DateTimeField(blank=True, null=True)
    #рейтинг вопроса (число)
    rating = models.IntegerField(default = 0)
    #автор вопроса
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #список пользователей, поставивших "лайк"
    likes = models.ManyToManyField(User, related_name = '+')
    def __unicode__(self):
        return self.title

# ответ
class Answer(models.Model):
    # текст ответа
    text = models.TextField()
    # дата добавления ответа
    added_at = models.DateTimeField(blank=True, null=True)
    # вопрос, к которому относится ответ
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    #автор ответа
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.text

