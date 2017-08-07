# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

from questions.models import UserProfile,Question,Answer,Tag,TagForQuestion
admin.site.register(Question)

class Qeustion(admin.ModelAdmin):
    fields=['question_text','header','author','rating']

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'

class UserAdmin(UserAdmin):
    inlines = (UserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
