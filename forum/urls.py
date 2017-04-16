from django.conf.urls import url

from . import views

app_name = 'forum'
urlpatterns = [

    url(r'^$', views.CategoryIndex.as_view(), name='category'), #shows all categories and their forums
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ThreadList.as_view(), name='forum'), #shows the forum and its threads
    url(r'^thread/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.PostList.as_view(), name='thread'),
   # url(r'^create_post/$', views.AddPost.as_view(), name='name'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/create_thread/$', views.AddThread.as_view(), name='add_thread')
    #(?P<pk>) passes the result of the regex into the var pk
]
