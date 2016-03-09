from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from models import Question, Answer
from forms import AskForm, AnswerForm
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required

#@login_required
def question_add(request):
    if request.method == "POST":
        #form = AskForm(request.user, request.POST)
        form = AskForm(request.POST)
        if form.is_valid(): 
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/question_add.html', {
        'form': form
    })        

#@login_required
def answer_add(request):
    if request.method == "POST":
        #form = AnswerForm(request.user, request.POST)
        form = AnswerForm(request.POST)
        if form.is_valid(): 
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'qa/answer_add.html', {
        'form': form
    })     

def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

def mainPage(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    limit = 10
    questions = Question.objects.order_by('-id')
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/mainPage.html', {
        'questions': page,
        'paginator': paginator, 'page': page,
    })

def popular(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    limit = 10
    questions = Question.objects.order_by('-rating')
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/popular.html', {
        'questions': page,
        'paginator': paginator, 'page': page,
    })

def question(request, slug):
    question = get_object_or_404(Question, id = slug)
    answers = Answer.objects.filter(question = question)
    return render(request, 'qa/question.html', {
        'question': question,
        'answers' : answers,
    })

    

    

    
    
     
