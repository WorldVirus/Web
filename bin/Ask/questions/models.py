from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
	user  = models.OneToOneField(User)
	avatar= models.ImageField(upload_to="avatar",verbose_name="photos")

class Question(models.Model):
	question_text = models.TextField()
	header = models.CharField(max_length = 50)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User)

	def best_questions(self):
		return self.filter(rating__gt=GOOD_RATING).order_by('-rating')

	def new_questions(self):
		return self.order_by('-created_at')


class Answer(models.Model):
	answer_text = models.CharField(max_length = 400)
	pub_date = models.DateTimeField('date publiched', )
	IsCorrect = models.IntegerField(default = 0)
	rating = models.IntegerField(default = 0)

class Tag(models.Model):
	tag_text = models.CharField(max_length = 10)

class TagForQuestion(models.Model):
	tag = models.ForeignKey(Tag)


class Like(models.Model):
	user= models.ForeignKey(User)
	is_like = models.BooleanField(default = True)
