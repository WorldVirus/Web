# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from questions.models import User,Question,Answer,Tag,TagForQuestion
# Register your models here.
"""
class AskInline(admin.StackedInline):
    model=Comments
    extra =2

class AskAdmin(admin.ModelAdmin):
    fields =['ask_title','ask_text','ask_date']
    inlines=[AskInline]
    list_filter = ['ask_date']

admin.site.register(Ask,AskAdmin)
"""
"""
# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserInline(admin.StackedInline):
    model = User
    can_delete = False
    verbose_name_plural = 'Доп. информация'

# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline, )

# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
"""
