from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecs_machine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vapor/', include('vapor.urls', namespace="vapor")),
    url(r'^deploy/', include('deploy.urls', namespace="deploy")),
)
