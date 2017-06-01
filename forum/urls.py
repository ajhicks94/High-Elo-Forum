from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'forum'
urlpatterns = [

    url(r'^$', views.CategoryIndex.as_view(), name='category'), #shows all categories and their forums
    url(r'^user/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.ThreadList.as_view(), name='forum'), #shows the forum and its threads
    url(r'^thread/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.PostList.as_view(), name='thread'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/create_thread/$', views.AddThread.as_view(), name='add_thread'),
    url(r'^thread/(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/create_post/$', views.AddPost.as_view(), name='add_post'),
    url(r'^create_user/$', views.CreateUser.as_view(), name='create_user'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/forum/logged_out/'}, name='logout'),
    url(r'^logged_out/$', views.LogOut.as_view(), name='logged_out'),
    #(?P<pk>) passes the result of the regex into the var pk
]
