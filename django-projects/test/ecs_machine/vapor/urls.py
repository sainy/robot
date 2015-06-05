from django.conf.urls import patterns, url

from vapor import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'query/',views.query, name='query'),
    
    )
