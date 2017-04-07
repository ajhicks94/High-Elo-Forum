from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Category, Forum, Thread, Post
from .forms import ThreadForm

#TODO: CLEAN UP OVER-IMPORTED LIBRARIES/ITEMS 

#need to show the categories and their subforums
class CategoryIndex(generic.ListView):
    model = Forum
    template_name = 'category.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.prefetch_related("forums").all()

#We've clicked on a forum and need to see its sub-forums if it has any,
#and its threads if it does not.
class ThreadList(generic.ListView):
    template_name = 'forum.html'
    context_object_name = 'thread_list'

    def get_context_data(self, **kwargs):
        context = super(ThreadList, self).get_context_data(**kwargs)
        forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        context['forum'] = forum
        return context

    def get_queryset(self):
        return Thread.objects.filter(forum=self.kwargs['pk'])

class PostList(generic.ListView):
    template_name = 'thread.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        thread = get_object_or_404(Thread, id=self.kwargs['pk'])
        context['thread'] = thread
        return context

    def get_queryset(self):
        return Post.objects.filter(thread=self.kwargs['pk'])

class AddThread(generic.FormView):
    form_class = ThreadForm
    success_url = '/forum/'
    template_name = 'add_thread.html'

    def form_valid(self, form):
        #DO STUFF HERE
        #new_Thread = Thread(title=form.fields['title'], body=form.fields['body'],
        #                    forum=get_object_or_404(Forum, name=form.fields['forum'].name), author='Admin')

        return super(AddThread, self).form_valid(form)


