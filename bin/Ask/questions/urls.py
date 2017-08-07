from django.conf.urls import include,url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

        url(r'^signup/?',views.signup, name='signup'),
        url(r'^registration/', views.registration, name='registration'),
        url(r'^ask/?', views.ask, name='ask'),
        url(r'^question/', views.question, name='question'),
        url(r'^settings/',views.settings,name ='settings'),
        url(r'^html_page/(\d+)/$', views.pagination_my,name ='index'),
        url(r'^tag_question/', views.tag_question, name='tag_question'),
        url(r'^answer/', views.answer, name='answer'),
        url(r'^best_answer/', views.best_answer, name='best_answer'),
        url(r'^base/', views.base, name='base'),
        url(r'^$', views.index, name='index'),
        url(r'^pageError/?', views.ask, name='ask'),
        url(r'^login/?', views.login, name='login'),
        url(r'^logout/?', views.logout, name='logout'),
        url(r'^like/?', views.like, name='like'),
        url(r'^page/(\d+)/$',views.index,name='index'),
                  ]
