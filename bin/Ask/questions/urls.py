from django.conf.urls import url
from . import views

urlpatterns = [
       # url(r'^$', views.post_list, name='post_list'),
        url(r'^$', views.index, name='index'),
        #url(r'^', views.settings, name='settings'),
        url(r'^login/', views.login, name='login'),
        url(r'^registration/', views.registration, name='registration'),
        url(r'^ask/', views.ask, name='ask'),
        url(r'^question/', views.question, name='question'),
        url(r'^settings/',views.settings,name ='settings'),
        url(r'^html_page/(\d+)/$', views.pagination_my,name ='index'),
        url(r'^tag_question/', views.tag_question, name='tag_question'),
        url(r'^answer/', views.answer, name='answer'),
        url(r'^best_answer/', views.best_answer, name='best_answer'),

                  ]
