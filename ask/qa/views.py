from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import Http404
from django.shortcuts import get_object_or_404
from models import Question, Answer
from django.core.paginator import Paginator, EmptyPage

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

    

    

    
    
     
