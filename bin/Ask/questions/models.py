# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	nickname = models.CharField(max_length = 20)
	email = models.CharField(max_length = 30)
	password = models.CharField(max_length = 20)
	rating = models.IntegerField(default = 0)
	avatar = models.CharField(max_length = 40)


class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	header = models.CharField(max_length = 50)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User)
	#tag
	def best_questions(self):
		return self.filter(rating__gt=GOOD_RATING).order_by('-rating')

	def new_questions(self):
		return self.order_by('-created_at')


class Answer(models.Model):
	question = models.ForeignKey(Question, related_name = 'answers')
	answer_text = models.CharField(max_length = 400)
	pub_date = models.DateTimeField('date publiched', )
	IsCorrect = models.IntegerField(default = 0)
	author = models.ForeignKey(User)
	rating = models.IntegerField(default = 0)

class Tag(models.Model):
	tag_text = models.CharField(max_length = 10)

class TagForQuestion(models.Model):
	tag = models.ForeignKey(Tag)
	question = models.ForeignKey(Question)

class Like(models.Model):
	user= models.ForeignKey(User)
	is_like=models.BooleanField()
