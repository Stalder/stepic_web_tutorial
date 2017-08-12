# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('added_at')

    def popular(self):
        return self.order_by('rating')


class Question(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)
    objects = QuestionManager()


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
