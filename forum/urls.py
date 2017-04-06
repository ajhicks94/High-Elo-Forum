from django.conf.urls import url

from . import views

app_name = 'forum'
urlpatterns = [

    url(r'^$', views.CategoryView.as_view(), name='category'), #shows all categories and their forums
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ForumView.as_view(), name='forum'), #shows the forum and its threads
    url(r'^thread/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ThreadView.as_view(), name='thread'),
   # url(r'^create_post/$', views.AddPostView.as_view(), name='name'),
    url(r'^create_thread/$', views.AddThreadView.as_view(), name='add_thread')
    #(?P<pk>) passes the result of the regex into the var pk
]
