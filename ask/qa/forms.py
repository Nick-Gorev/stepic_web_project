#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from models import Question, Answer

# форма добавления вопроса
class AskForm(forms.Form):
    # Поля формы
    #title - поле заголовка
    title = forms.CharField(max_length=255)
    #text - поле текста вопроса
    text = forms.CharField(widget=forms.Textarea)
    # переопределяем конструктор формы и запоминаем текущего пользователя
    #def __init__(self, user, **kwargs):
    #    self._user = user
    #    super(AskForm, self).__init__(**kwargs)
    def save(self):
    #    self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        self._url = question.get_url()
        return question            
    def get_url(self):
        return self._url
    

# форма добавления ответа
class AnswerForm(forms.Form):
    # Поля формы
    #text - поле текста ответа
    text = forms.CharField(widget=forms.Textarea)
    #question - поле для связи с вопросом
    question = forms.IntegerField()
    # дополнительная валидация поля question
    # проверка, действительно ли есть такой вопрос
    def clean_question(self):
        question = Question.objects.filter(pk = self.cleaned_data['question'])
        if len(question[:]) <= 0:
            raise forms.ValidationError(u'Такого вопроса не существует', code=12)
        return question[0]        
    # переопределяем конструктор формы и запоминаем текущего пользователя
    #def __init__(self, user, **kwargs):
    #    self._user = user
    #    super(AnswerForm, self).__init__(**kwargs)
    def save(self):
    #    self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        self._url = answer.get_url()
        return answer            
    def get_url(self):
        return self._url

