from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Category, Forum, Thread, Post
from .forms import NameForm

#TODO: REMOVE *VIEW SUFFIX, WERE IN THE FUCKING VIEWS FILE, OFC IT'S A VIEW
#TODO: CLEAN UP OVER-IMPORTED LIBRARIES/ITEMS
#
#
#
#
#
#
#
#






#need to show the categories and their subforums
class CategoryView(generic.ListView):
    model = Forum
    template_name = 'category.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.prefetch_related("forums").all()

#We've clicked on a forum and need to see its sub-forums if it has any,
#and its threads if it does not.
class ForumView(generic.ListView):
    template_name = 'forum.html'
    context_object_name = 'thread_list'

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        context['forum'] = forum
        return context

    def get_queryset(self):
        return Thread.objects.filter(forum=self.kwargs['pk'])

class ThreadView(generic.ListView):
    template_name = 'thread.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        thread = get_object_or_404(Thread, id=self.kwargs['pk'])
        context['thread'] = thread
        return context

    def get_queryset(self):
        return Post.objects.filter(thread=self.kwargs['pk'])

class TopicIndexView(generic.ListView):
    template_name = 'topic_index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.filter(modified_on__lte=timezone.now()).order_by('-modified_on')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'

class AddPostView(generic.FormView):
    form_class = NameForm #CHANGE THIS FORM
    success_url = '/forum/'
    template_name = 'name.html'

    def form_valid(self, form):
        #DO STUFF HERE
        #form.send_email()
        return super(AddPostView, self).form_valid(form)
