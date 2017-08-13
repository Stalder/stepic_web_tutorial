# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('rating')


class Question(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='author')
    likes = models.ManyToManyField(User, related_name='likes')
    objects = QuestionManager()

    def __unicode__(self):
        return self.title

    def get_url(self):
        return reverse('qa:question', kwargs={'question_id': self.pk})


class AnswerManager(models.Manager):
    def for_this_question(self, question):
        return self.filter(question=question)


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
