from django.http import HttpResponse,HttpResponseNotFound, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from questions.models import UserProfile,Question,TagForQuestion,Answer,Tag,Like
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from questions.forms import UserForm,QuestionForm
from django.contrib.auth.models import User
from django.contrib import auth
import json
import datetime

def tag_question(request):
    return render(request, 'questions/tag_question.html', {})

def best_answer(request):
    return render(request,'questions/best_answer.html',{})

def answer(request):
    return render(request,'questions/answer.html',{})

def settings(request):
    return render(request, 'questions/settings.html',{})

def signup(request):
    if request.POST:
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           form.save_image()
           return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'questions/signup.html',{'form':form})
    else:
        form = UserForm()
    return render(request, 'questions/signup.html',{'form':form})

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'questions/login.html',{'login_error':True})
    else:
        return render(request,'questions/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def registration(request):
    return render(request, 'questions/registration.html',{})


def ask(request):
    if request.user.is_authenticated:
        if request.POST:
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save()
                return redirect('/')
        else:
            form= QuestionForm()
    else:
        return render(request,'questions/pageError.html')
    return render(request, 'questions/ask.html',{'form':form})

def question(request):
    return render(request, 'questions/question.html',{})

def base(request):
    return render(request, 'questions/base.html',{})


def pagination_my(request, iterable, page_size=30):
    paginator = Paginator(iterable, page_size)
    page_num = request.GET.get('page')

    try:
        obj_list = paginator.page(page_num)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_pages)
    return obj_list


def newest_list_page_view(request, *args, **kwargs):
    articles = models.Article.objects.get_newest()
    return render(request, 'index.html',{
        'obj_list': pagination_my(request, articles),
    })


def index(request,page_number=1):
    all_questions=Question.objects.all()
    current_page = Paginator(all_questions,2)
    return render(request,'questions/index.html',{'questions':current_page.page(page_number)})

def like(request):
    q_id = request.POST['q_id']
    user = request.user
    try:
        question = Question.objects.get(request.POST.get('q_id'))
        Like.objects.create(user=request.user,question=question).count()
        return HttpResponse(json.dumps({
            'status':'ok',
            'likes':len(question.vote_set),
        }),content_type='application/json'
        )
    except:
        return HttpResponse(json.dump({
            'status':'error',

        }),content_type='application/json'
        )
