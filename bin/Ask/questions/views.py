from django.http import HttpResponse,HttpResponseNotFound, Http404
#from django.http import QueryDict
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from questions.models import User,Question,TagForQuestion,Answer
from django.shortcuts import get_object_or_404

"""
def post_list(request):
    return render(request, 'questions/post_list.html', {})

    ZACOMENCHENNAY FUNKCIY
def post_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        return render(request, 'questions/post_detail.html' , {'form': form})
    else:
        form = PostForm()
        return render(request, 'questions/post_detail.html', {'form': form})
"""
def tag_question(request):
    return render(request, 'questions/tag_question.html', {})

def best_answer(request):
    return render(request,'questions/best_answer.html',{})

def answer(request):
    return render(request,'questions/answer.html',{})
def index(request):
    return render(request, 'questions/index.html', {})

def settings(request):
    return render(request, 'questions/settings.html',{})

def login(request):
    return render(request, 'questions/login.html',{})

def registration(request):
    return render(request, 'questions/registration.html',{})

def ask(request):
    return render(request, 'questions/ask.html',{})

def question(request):
    return render(request, 'questions/question.html',{})




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

def paginate_lection(request, qs):
    try:
        limit = int(request.GET.get('limit', 5))
    except ValueError:
        limit = 5
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
"""
def index(request):
        return render(request, 'questions/index.html', {'Question':questions.objects()})


def index (request):
    context['question'] = pager.page(page).object_list
    context['pager'] = pager
    context['tags'] = Question.objects.all().values('id', 'tag__tag_text')
    context['popular_tags'] = Tag.objects.all().values('tag_text').annotate(Count("question")).order_by('-question__count')[0:5]
    context['best_users'] = User.objects.all().order_by('-profile__rating')[0:5]
    return render(req, 'index.html', context)

"""
