from django.conf.urls import patterns, url

from tasks import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^edit/', views.edit, name='edit'),
                       url(r'^view_requests/', views.view_requests, name='view_requests'),
                       url(r'^login/', views.login, name='login'),
                       url(r'^logout/', views.logout, name='logout'),
                       )
