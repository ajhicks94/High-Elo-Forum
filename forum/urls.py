from django.conf.urls import url

from . import views

app_name = 'forum'
urlpatterns = [

    url(r'^$', views.CategoryView.as_view(), name='category'), #shows all categories and their forums
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ForumView.as_view(), name='forum'), #shows the forum and its threads
    url(r'^thread/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ThreadView.as_view(), name='thread')
    #(?P<pk>) passes the result of the regex into the var pk
    #url(r'^testtopic/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')    
]
