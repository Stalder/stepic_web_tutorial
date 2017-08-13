# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Answer

# Create your views here.


def main(request):
    questions = Question.objects.new()
    page = request.GET.get('page', 1)
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'main.html', {
        'questions': page.object_list
    })


def popular(request):
    questions = Question.objects.popular()
    page = request.GET.get('page', 1)
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'popular.html', {
        'questions': page.object_list
    })


def question_details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404
    answers = Answer.objects.for_this_question(question)

    return render(request, 'question.html', {
        'question': question,
        'answers': answers
    })
