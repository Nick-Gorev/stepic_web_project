#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Форма входа существующего пользователя
class LoginForm(forms.Form):
    # имя пользователя, логин
    username = forms.CharField(max_length=255) 
    # пароль пользователя
    password = forms.CharField(max_length=255)
    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is None:
            raise forms.ValidationError('Invalid login')    
    def save(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        return user

# Форма регистрации нового пользователя
class SignupForm(forms.Form):
    # имя пользователя, логин
    username = forms.CharField(max_length=255) 
    # email пользователя
    email = forms.EmailField(max_length=255) 
    # пароль пользователя
    password = forms.CharField(max_length=255)
    #def clean(self):
    #    username = self.cleaned_data['username'];
    #    if User.objects.filter(username=username).exists():        
    #        raise forms.ValidationError('User ' + username + ' aready exist.')    
    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        return user

# форма добавления вопроса
class AskForm(forms.Form):
    # Поля формы
    # поле заголовка
    title = forms.CharField(max_length=255)
    # поле текста вопроса
    text = forms.CharField(widget=forms.Textarea)
    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        self._url = question.get_url()
        return question            
    def get_url(self):
        return self._url
    

# форма добавления ответа
class AnswerForm(forms.Form):
    # Поля формы
    # поле текста ответа
    text = forms.CharField(widget=forms.Textarea)
    # поле для связи с вопросом
    question = forms.IntegerField()
    # дополнительная валидация поля question
    # проверка, действительно ли есть такой вопрос
    def clean_question(self):
        question = Question.objects.filter(pk = self.cleaned_data['question'])
        if len(question[:]) <= 0:
            raise forms.ValidationError(u'Такого вопроса не существует', code=12)
        return question[0]        
    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        self._url = answer.get_url()
        return answer            
    def get_url(self):
        return self._url

