from django.conf.urls import patterns, url
from deploy import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'index/', views.index, name='index'),
    url(r'addItem/', views.addItem, name='addItem'),
    url(r'saveItem/', views.saveItem, name='saveItem'),
    url(r'savevar/', views.saveVariable, name='saveVariable'),
    url(r'(?P<sheet_name>.+)/instance', views.instance, name='instance'),
    url(r'(?P<sheet_name>.+)/deploy', views.deploy, name='deploy'),
    url(r'(?P<sheet_name>.+)/variable', views.variable, name='variable'),
)

