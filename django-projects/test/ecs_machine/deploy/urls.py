from django.conf.urls import patterns, url
from deploy import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'addItem/', views.addItem, name='addItem'),
    url(r'saveItem', views.saveItem, name='saveItem'),
    url(r'addItem/addvar', views.saveVariable, name='saveVariable'),
)

