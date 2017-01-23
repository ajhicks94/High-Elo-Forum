from django.conf.urls import url

from . import views

app_name = 'forum'
urlpatterns = [

    url(r'^$', views.CategoryView.as_view(), name='category'),
    #url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ForumView.as_view(), name='forum'),
    #url(r'^category/$', views.TopicIndexView.as_view(), name='index'),
    #(?P<pk>) passes the result of the regex into the var pk
    #url(r'^testtopic/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')    
]
